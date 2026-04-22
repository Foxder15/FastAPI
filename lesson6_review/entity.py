import hashlib
import uuid

class User:
    def __init__(self,id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def __str__(self) -> str:
        return f"ID: {self.id}\nName: {self.name}\nPassword: {self.password}"
    

def mockup_data() -> None:
    with open('mockup.txt', 'r') as f:
        users = [f'{uuid.uuid1()}, {line.split(',')[0].strip()}, {line.split(',')[1].strip()}\n' for line in f]
        with open('users.txt', 'w') as f:
            f.writelines(users)

if __name__ == "__main__":
    # user: User = User('Baku', '@12345')
    # print(user)
    mockup_data()