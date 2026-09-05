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
mem1 = sum([sys.getsizeof(el) + sys.getsizeof(el.__dict__) for el in list1])
list2 = [SlotUser('Alex', 'a@mail.ru', '123$') for i in range(0, 100_000)]
mem2 = sum([sys.getsizeof(el) for el in list2])

print(mem1, mem2)


