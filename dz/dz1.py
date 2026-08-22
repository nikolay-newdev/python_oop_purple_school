"""Домашнее задание по курсу ООП, Банковский Счет"""

class BankAccount:
    """Банковский счет"""
    accounts: int = 0

    def __init__(self, owner: str, number: str|int, balance: float = 0):
        self.owner = owner
        self.number = number
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        else:
            self.balance = balance
        BankAccount.accounts += 1

    def deposit(self, amount: float):
        """Положить деньги на счет"""
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Пополнение должно быть положительным")
        return self.balance

    def withdraw(self, amount: float):
        """Снять деньги со счета"""
        if self.balance < amount:
            raise ValueError("Сумма снятия превышает баланс")
        else: 
            self.balance -= amount
        return self.balance

    def transfer_to(self, other_account: BankAccount, amount: float):
        """Перевод денег на другой счет"""
        if self.balance < amount:
            raise ValueError("Сумма перевода превышает баланс")
        else:
            self.balance -= amount
            other_account.deposit(amount)
        return self.balance

    def info(self):
        """Информация о счете"""
        return f"Владелец: {self.owner}, Номер счета: {self.number}, Баланс: {self.balance}"

    @classmethod
    def get_accounts_created(cls):
        """Количество созданных счетов"""
        return cls.accounts

account1 = BankAccount('Nikolay', 1)
print(account1.info())
print(BankAccount.get_accounts_created())
print('---')

account1.deposit(100)
print(account1.info())

account1.withdraw(50)
print(account1.info())

account2 = BankAccount('Olga', 2, 200)
print(account2.info())
print(BankAccount.get_accounts_created())
print('---')

account1.transfer_to(account2, 25)
print(account1.info())
print(account2.info())
print(BankAccount.get_accounts_created())
print('---')




#EOF