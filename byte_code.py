class ByteCode():
    def __init__(self, file_addr: str) -> None:
        self.addr = file_addr
        self.commands = []
        with open(file_addr) as f:
            for line in f:
                self.commands.append(line.strip())

        f.close()
    
    def get_commands(self):
        return self.commands