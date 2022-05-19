import sys
from byte_code import *

class Interpreter():
    def __init__(self) -> None:
        self.ip = 0
        self.stack = []
        self.env = {}
        self.commands = None
        self.frames = []

    def peek(self):
        return self.stack.pop()
    
    def LOAD_VAL(self, val):
        self.stack.append(int(val))

    def WRITE_VAR(self, name):
        val = self.stack.pop()   
        self.env[name] = val

    def READ_VAR(self, name):
        if name not in self.env:
            raise NameError("name: {name} is undefined")
        val = self.env[name]
        self.stack.append(val)
    
    def ADD(self, _):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def SUBTRACT(self, _):
        self.stack.append(self.stack.pop() - self.stack.pop())

    def MULTIPLY(self, _):
        self.stack.append(self.stack.pop() * self.stack.pop())

    def DIVIDE(self, _):
        self.stack.append(self.stack.pop() / self.stack.pop())
    
    def ISEQ(self, _):
        self.stack.append(self.stack.pop() == self.stack.pop())

    def JMP(self, _):
        addr = self.stack.pop()
        if isinstance(addr, int) and 0 <= addr < len(self.commands):
            self.ip = addr
        else:
            raise RuntimeError("JMP address must be valid")
    
    
    def JIF(self, _):
        addr = self.stack.pop()
        cond = self.stack.pop()
        if(cond):
            self.ip = addr

    def HALT(self, _):
        print("Halt reached")


    def __call__(self, commands) -> None:
        self.commands = commands
        
        fmap = {
            'LOAD_VAL': self.LOAD_VAL,
            'WRITE_VAR': self.WRITE_VAR,
            'READ_VAR': self.READ_VAR,
            "ADD": self.ADD,
            "SUBTRACT": self.SUBTRACT,
            "MULTIPLY": self.MULTIPLY,
            "DIVIDE": self.DIVIDE,
            "ISEQ": self.ISEQ,
            "JMP": self.JMP,
            "JIF": self.JIF,
            "HALT": self.HALT
        }
        
        while self.ip < len(self.commands):
            opcode, _,  oparg = self.commands[self.ip].partition(' ')             

            fmap[opcode](oparg)

            self.ip += 1
        # print(self.stack)

if __name__ == '__main__':
    
    if (len(sys.argv) > 1):
      intp = Interpreter()
      file_addr = sys.argv[1]
      byte_code = ByteCode(file_addr)
      intp(byte_code.commands)
      print(intp.peek())
    else:
        intp = Interpreter()
        if_addr = "test/if.txt"
        if_byte_code = ByteCode(if_addr)
        intp(if_byte_code.commands)
        assert 4 == intp.peek()
        
        intp = Interpreter()
        loop_addr = "test/loop.txt"
        loop_byte_code = ByteCode(loop_addr)
        intp(loop_byte_code.commands)
        assert 25 == intp.peek()
    
