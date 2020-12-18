import re


class TokenType:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"


class Number(TokenType):
    def __get__(self, obj):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        setattr(obj, self.name, int(value))


class String(TokenType):
    def __get__(self, obj):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if value and len(value) != self.size:
            raise Exception(f"String size value mismatch for {self.name}. Expected {self.size}, got {len(value)}")
        setattr(obj, self.name, value)


class PasswordEntry:
    regex = re.compile(r"(?P<l>\d+)-(?P<r>\d+) (?P<letter>\w): (?P<password>\w+)")
    l = Number()
    r = Number()
    letter = String()
    password = String()

    def __init__(self, password_entry):
        for name, value in self.regex.match(password_entry).groupdict().items():
            self.__setattr__(name, value)
