class Frame():
    def __init__(self, return_address) -> None:
        self.return_address = return_address
        self.env = {}

    def write_var(self, var_name, var_value):
        self.env[var_name] = var_value

    def read_var(self, var_name):
        return self.env[var_name]

    def get_return_address(self):
        return self.return_address

    def get_variables(self):
        return self.env