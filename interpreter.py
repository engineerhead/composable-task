import sys
from byte_code import *
from frame import *

class Interpreter():
    def __init__(self) -> None:
        self.ip = 0
        self.stack = []
        self.env = {}
        self.commands = None
        self.frames = []
        self.frames.append(Frame(0))
        # self.frames.

    def get_current_frame(self):
        return self.frames[-1]

    def peek(self):
        return self.stack.pop()
    
    def LOAD_VAL(self, val):
        self.stack.append(int(val))

    def WRITE_VAR(self, name):
        val = self.stack.pop() 
        self.get_current_frame().env[name] = val
        # self.env[name] = val

    def READ_VAR(self, name):
        # if name not in self.env:
            # raise NameError("name: {name} is undefined")
        # val = self.env[name]
        val = self.get_current_frame().env[name]
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
    
    def CALL(self, _):
        address = self.stack.pop()
        self.frames.append(Frame(self.ip))
        self.ip = address
        

    def RETURN_VAL(self,_):
        return_address = self.get_current_frame().get_return_address()
        self.frames.pop()
        self.ip = return_address
       

    def HALT(self, _):
        print("Halt reached")
        self.commands = []

    def DEBUG(self, _):
        print("In debug")


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
            "HALT": self.HALT,
            "CALL": self.CALL,
            "RETURN_VAL": self.RETURN_VAL,
            "DEBUG": self.DEBUG
        }
        
        while self.ip < len(self.commands):
            opcode, _,  oparg = self.commands[self.ip].partition(' ')             

            fmap[opcode](oparg)

            self.ip += 1

if __name__ == '__main__':
    
    if (len(sys.argv) > 1):
      intp = Interpreter()
      file_addr = sys.argv[1]
      byte_code = ByteCode(file_addr)
      intp(byte_code.commands)
      print(intp.peek())
    else:
        intp = Interpreter()
        func_addr = "test/func.txt"
        func_byte_code = ByteCode(func_addr)
        intp(func_byte_code.commands)
        assert 3 == intp.peek()

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
    
