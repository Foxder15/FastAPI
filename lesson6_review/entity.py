import hashlib
import uuid

class User:
    def __init__(self,id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def __str__(self) -> str:
        return f"ID: {self.id}\nName: {self.name}\nPassword: {self.password}"