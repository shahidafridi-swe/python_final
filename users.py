class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, name, email, password, phone, address,account_type) -> None:
        super().__init__(name, email, password)
        self.phone = phone
        self.address = address
        self.account_type = account_type
        self.__balance = 0.0
        self.__loan_amount = 0.0
        self.loan_quantity = 0
        self.id = self.name[0:3] + self.phone + self.name[-3:]
        self.transactions = []


    def deposit(self,bank, amount):
        bank.deposit(self, amount)

    def withdraw(self,bank, amount):
        bank.withdraw(self, amount)

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        self.__balance = value

    @property
    def loan_amount(self):
        return self.__loan_amount
    
    @loan_amount.setter
    def loan_amount(self,value):
        self.__loan_amount = value

    def transaction_history(self):
        print("\n\tTransaction History")
        print("-------------------------------------------------------------")
        print("Type\t\t\tAmount\t\tTime")
        print("-------------------------------------------------------------")
        for t in self.transactions:
            print(f"{t.type} \t\t{t.amount} BDT\t{t.time}")                

    def take_loan(self,bank, amount):
        bank.take_loan(self, amount)

    def transfer_money(self,bank, reciver_name, reciver_phone, amount):
        bank.transfer_money(self, reciver_name,reciver_phone, amount)



class Admin(User):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)

    def add_customer(self, bank, customer):
        bank.add_customer(customer)

    def delete_customer(self, bank, customer_name, customer_phone):
        bank.delete_customer(customer_name, customer_phone)

    def view_all_customer(self, bank):
        bank.view_all_customer()

    def total_bank_balance(self, bank):
        return bank.balance

    def total_loan_amount(self, bank):
        return bank.loan_amount

    def control_loan_activity(self, bank,value):
        bank.control_loan_activity(value)

    def control_bankrupt(self, bank,value):
        bank.control_bankrupt(value)

