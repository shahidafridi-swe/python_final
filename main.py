from bank import Bank
from users import Admin, Customer

aBank = Bank("Ayman Bnak")

admin = Admin("admin", 'admin@abank.com', '123')
aBank.add_admin(admin)


currentUser = None
while True:
    print(f"\n\t Welcome to {aBank.name}")
    print("----------------------------------------------------------")
    print("\nAre Admin or Customer ?")
    print("Press 1 : for admin")
    print("Press 2 : for customer")
    print("Press 0 : for end the program")
    opUser = input("\n\tPlease enter here : ")

    if opUser == '0':
        print("Thank you for staying with us.")
        break
    
    #Admin UI
    elif opUser == '1':
        print("\nName: admin , Password: 123 -> for admin login")
        name = input("\tEnter the name: ")
        password = input("\tEnter the password: ")
        
        for admin in aBank.admins:
            if admin.name == name and admin.password == password:
                currentUser = admin
                break
        if not currentUser:
            print("Invalid information, Try Again !!!")
        else:
            while True:
                print("\nHello Admin...")
                print("\nOptions:")
                print("\t 1. Add Customer")
                print("\t 2. Delete Customer")
                print("\t 3. View All Customer")
                print("\t 4. Check Total Bank Balance")
                print("\t 5. Check Total Loan Amount")
                print("\t 6. Control Loan Avtivation")
                print("\t 7. Control Bankrupt")
                print("\t 0. Log Out")

                op = input("\nPlease enter your choice: ")

                if op == '1':
                    name = input("Enter the name: ")
                    email = input("Enter the email: ")
                    password = input("Enter the password: ")
                    phone = input("Enter the phone: ")
                    address = input("Enter the address: ")
                    account_type = input("Account Type -> Savings / Current : \n\t Press -> 'S' for Savings or Press -> 'C' for Current : ")
                    if account_type.lower() == 's':
                        account_type = "Savings"
                    elif account_type.lower() == 'c':
                        account_type = "Current"
                    else:
                        print("Please enter right information of account type and try again !")
                        continue
                    customer = Customer(name,email,password,phone,address,account_type)
                    currentUser.add_customer(aBank, customer)

                elif op == '2':
                    name = input("Enter the name: ")
                    phone = input("Enter the phone: ")
                    currentUser.delete_customer(aBank,name,phone)


                elif op == '3':
                    currentUser.view_all_customer(aBank)

                elif op == '4':
                    balance = currentUser.total_bank_balance(aBank)
                    print(f"Total Balance of {aBank.name} is : {balance} BDT")

                elif op == '5':
                    loan = currentUser.total_loan_amount(aBank)
                    print(f"Total Loan Amount of {aBank.name} is : {loan} BDT")


                elif op == '6':
                    if aBank._loanActive:
                        print("At this moment the loan facilities is 'ACTIVE'.")
                        x = input("If you want to 'INACTIVE' then type 'off' otherwise type anything to ignore : ")
                        if x.lower() == 'off':
                            currentUser.control_loan_activity(aBank,False)
                            print("\n\tNow the loan facilities is 'INACTIVE'.")

                    else:
                        print("At this moment the loan facilities is 'INACTIVE'.")
                        x = input("If you want to 'ACTIVE' then type 'on' otherwise type anything to ignore : ")
                        if x.lower() == 'on':
                            currentUser.control_loan_activity(aBank,True)
                            print("\n\tNow the loan facilities is 'ACTIVE'.")

                            
                elif op == '7':
                    if aBank._isBunkrupt:
                        print("At this moment the 'Bank is Bankrupt'")
                        x = input("If you want to 'INACTIVE' the Bankrupt then type 'off' otherwise type anything to ignore : ")
                        if x.lower() == 'off':
                            currentUser.control_bankrupt(aBank,False)
                            print("\n\tNow the 'Bank is NOT Bankrupt'")

                    else:
                        print("At this moment the 'Bank is NOT Bankrupt' ")
                        x = input("If you want to 'ACTIVE' Bankrupt then type 'on' otherwise type anything to ignore : ")
                        if x.lower() == 'on':
                            currentUser.control_bankrupt(aBank,True)
                            print("\n\tNow the 'Bank is Bankrupt'")

                elif op == '0':
                    currentUser = None
                    break
                    
                else:
                    print("\t !!! Invalid Input !!!")


    #Customer UI
    elif opUser == '2':
        while True:
            print("\nHello Sir/Madam...")
            print("Do you want to Login or Register ?")
            print("Press 1 : for Login")
            print("Press 2 : for Register")
            print("Press 0 : for Main Menu")
            opLR = input("\n\tPlease enter here : ")
            
            if opLR == '0':
                break

            elif opLR == '1': #login
                email = input("\nEnter your email: ")
                password = input("Enter your password: ")
                for cus in aBank.customers:
                    if cus.email == email and cus.password == password:
                        currentUser = cus
                        break
                if not currentUser:
                    print('\n\tUser not found !!!')
                

            elif opLR == '2': #register
                name = input("\nEnter the name: ")
                email = input("Enter the email: ")
                password = input("Enter the password: ")
                phone = input("Enter the phone: ")
                address = input("Enter the address: ")
                account_type = input("Account Type -> Savings / Current : \n\t Press -> S for Savings or Press 'C' for Current : ")
                if account_type.lower() == 's':
                    account_type = "Savings"
                elif account_type.lower() == 'c':
                    account_type = "Current"
                else:
                    print("Please enter right information of account type and try again !")
                    continue
                customer = Customer(name,email,password,phone,address,account_type)
                aBank.add_customer( customer)
            
            else:
                print("\t !!! Invalid Input !!!")   

            if currentUser:
                while True:
                    print(f"\nHello {currentUser.name} !!!")
                    print("Options:")
                    print("\t 1. Check Balance")
                    print("\t 2. Deposit")
                    print("\t 3. Withdraw")
                    print("\t 4. Transfer Money")
                    print("\t 5. Take Loan")
                    print("\t 6. Transaction History")
                    print("\t 0. Log Out")

                    op = input("\nPlease enter your choice: ")
                    print(" ")
                    if op == '1':
                        balance =currentUser.balance
                        print(f"Your Current Balance : {balance} BDT")
                    elif op == '2':
                        try:
                            amount = float(input("How much you want to deposit: "))
                            currentUser.deposit(aBank, amount)  
                        except:
                            print("\n\tThe amount should be must numeric value !!!")  

                    elif op == '3':
                        try:
                            amount = float(input("How much you want to withdraw: "))
                            currentUser.withdraw(aBank, amount)
                        except:
                            print("\n\tThe amount should be must numeric value !!!")  

                    elif op == '4':
                        try:
                            reciver_name = input("Enter the reciver name: ")
                            reciver_phone = input("Enter the reciver phone number: ")
                            amount = float(input("How much you want to transfer: "))
                            currentUser.transfer_money(aBank, reciver_name,reciver_phone, amount)
                        except:
                            print("\n\tThe amount should be must numeric value !!!")

                    elif op == '5':
                        try:
                            amount = float(input("How much you want to take loan: "))
                            currentUser.take_loan(aBank, amount)
                        except:
                            print("\n\tThe amount should be must numeric value !!!")  

                    elif op == '6':
                        currentUser.transaction_history()
                     
                    elif op == '0':
                        currentUser = None
                        break
                    else:
                        print("\t !!! Invalid Input !!!")
        
    else:
        print("\t !!! Invalid Input !!!")



