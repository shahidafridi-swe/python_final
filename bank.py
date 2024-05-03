from datetime import datetime

class Transaction:
    def __init__(self, type, amount) -> None:
        self.type = type
        self.amount = amount
        self.time = datetime.now()

class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.customers = []
        self.admins= []
        self.__balance = 0.0
        self.__loan_amount = 0.0
        self._loanActive = True
        self._isBunkrupt = False


# Customer Activities
    def deposit(self, customer, amount):
        if amount > 0:
            if customer in self.customers:
                customer.balance += amount
                self.__balance += amount
                transaction = Transaction('Deposit',amount)
                customer.transactions.append(transaction)
                print(f"{amount} BDT deposit successfull!!")
            else:
                print(f"Name: {customer.name} and Phone: {customer.phone} , This person is not found !!!")
        else:
            print("Amount should be greater than 0")
    
    def withdraw(self, customer, amount):
        if not self._isBunkrupt:
            if amount > 0:
                if customer in self.customers:
                    if amount <= customer.balance:
                        customer.balance -= amount
                        self.__balance -= amount
                        transaction = Transaction('Withdraw',amount)
                        customer.transactions.append(transaction)
                        print(f"{amount} BDT withdraw successfull!!")
                    else:
                        print("Withdraw amount exceeded !!!")
                else:
                    print(f"Name: {customer.name} and Phone: {customer.phone} , This person is not found !!!")
            else:
                print("Amount should be greater than 0")
        else:
            print("Sorry ! At this moment bank is 'bankrupt'. You can't withdraw now, Try again later !'")
    
    def take_loan(self, customer, amount):
        if not self._isBunkrupt:
            if self._loanActive:
                if customer.loan_quantity < 2:
                    customer.balance += amount
                    self.balance += amount
                    self.loan_amount += amount
                    customer.loan_quantity += 1
                    transaction = Transaction('Got_Loan',amount)
                    customer.transactions.append(transaction)
                    print(f"Congratulations! You got loan: {amount} BDT.")
                else:
                    print("You already took loan 2 times. You can't take more loan at this moment.")
            else:
                print("Sorry ! At this moment loan facilities is 'INACTIVE. Try again later !'")
        else:
            print("Sorry ! At this moment bank is 'bankrupt'. You can't take loan now, Try again later !'")
            
    def transfer_money(self, sender, reciver_name, reciver_phone, amount):
        if amount <=0:
            print("Transfer amount should be greater than 0")
        elif amount <= sender.balance:
            reciver = self.find_customer(reciver_name, reciver_phone)
            if reciver:
                reciver.balance += amount
                sender.balance -= amount
                senderTransaction = Transaction('Transfer',amount)
                reciverTransaction = Transaction('Recived',amount)
                sender.transactions.append(senderTransaction)
                reciver.transactions.append(reciverTransaction)

                print(f"{amount} BDT transfered to {reciver_name} successfully!")
            else:
                print(f"{reciver_name} name of reciver not found!")
        else:
            print("\n\tTransfer amount exceeded !!!")      
    

# Admin Activities
    def add_admin(self, admin):
        self.admins.append(admin)

    def add_customer(self, customer):
        for cus in self.customers:
            if customer.name == cus.name and customer.phone == cus.phone:
                print(f"Name: {customer.name} and Phone: {customer.phone} , This person already have an acoount. Try Another !")
                return
        self.customers.append(customer)
        print(f"\nName: {customer.name} and Phone: {customer.phone}, this account created successfully !\n")
        
    def control_loan_activity(self, value):
        self._loanActive = value

    def control_bankrupt(self,value):
        self._isBunkrupt = value
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def loan_amount(self):
        return self.__loan_amount
    
    @loan_amount.setter
    def loan_amount(self, value):
        self.__loan_amount = value
    
    def view_all_customer(self):
        print("\n\tAll Customers")
        print("-----------------------------------------------------------------")
        print("Name\t\tPhone\t\tAddress\t\tLoan_Taken\tBalance")
        print("-----------------------------------------------------------------")
        for customer in self.customers:
            print(f"{customer.name}\t{customer.phone}\t{customer.address}\t{customer.loan_quantity}\t\t{customer.balance} BDT")

    def find_customer(self, customer_name, customer_phone):
        for cus in self.customers:
            if customer_name == cus.name and customer_phone == cus.phone:
                # print(f"Name: {customer_name} and Phone: {customer_phone} , This person is not found !!!")
                return cus
        return None

    def delete_customer(self,customer_name, customer_phone):
        isCustomer = self.find_customer(customer_name,customer_phone)
        if isCustomer:
            self.balance -= isCustomer.balance
            self.loan_amount -= isCustomer.loan_amount
            self.customers.remove(isCustomer)
            print(f"Name: {customer_name} and Phone: {customer_phone} , This person's account deleted !!!")
        else:
            print(f"Name: {customer_name} and Phone: {customer_phone} , This person is not found !!!")

     
