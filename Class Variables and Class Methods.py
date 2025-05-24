class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Usage
bank1 = Bank()
bank2 = Bank()
print(bank1.bank_name)  # Default Bank

Bank.change_bank_name("New Bank")
print(bank2.bank_name)  # New Bank