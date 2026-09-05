from dataclasses import dataclass
import sys


@dataclass
class User:
    name: str
    email: str
    password: str

class SlotUser:
    __slots__ = ('name', 'email', 'password')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

list1 = [User('Alex', 'a@mail.ru', '123$') for i in range(0, 100_000)]
list2 = [SlotUser('Alex', 'a@mail.ru', '123$') for i in range(0, 100_000)]

print(sys.getsizeof(list1))
print(sys.getsizeof(list2))