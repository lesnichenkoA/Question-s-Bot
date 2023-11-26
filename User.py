class User:
    def __init__(self, name):
        self.name = name
        self.number = None
        self.email = None
        self.address = None

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def set_name(self, new_name):
        self.name = new_name