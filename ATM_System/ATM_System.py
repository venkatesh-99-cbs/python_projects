from abc import ABC, abstractmethod


#======================>Abstract Class<==========================#

class BankAccount(ABC):
    @abstractmethod
    def Transction(self):
        pass



#======================> Base Class <==========================#

class Account:
    def __init__(self, A_name, A_number, A_amount, pin):
        self.Holder_Name = A_name
        self._Holder_Account_number = A_number
        self.__Holder_Amount = A_amount
        self.__PIN = pin
        self.Transaction_Count = 0
        self.Transaction_History = []

    def get_Amount(self):# object methods to access the private variable value
        return self.__Holder_Amount

    def set_Amount(self, amount):# to update the Private variable value
        self.__Holder_Amount = amount

    def verify_pin(self, pin): # pin verification
        return self.__PIN == pin

    def Account_detials(self): # to display the Account Holder Details
      print(f"Holder Name =>{self.Holder_Name}")
      print(f"Holder Account  Number =>{self._Holder_Account_number}")
      print(f"Holder Transcation =>{self.Show_Transaction_History()}")




#======================>Child Class<==========================#

class A_T_M(BankAccount, Account):

    MAX_WITHDRAW_LIMIT = 10000 # To  prevent the user from withdrawing large amount

    def __init__(self, A_name, A_number, A_amount, pin):
        Account.__init__(self, A_name, A_number, A_amount, pin)

    def Amount(self, amount): # for update the amount in transaction operations
        balance = self.get_Amount() + amount
        self.set_Amount(balance)
        return balance

    def Check_balance(self):
        print(f"Your account balance is: ₹{self.get_Amount()}")

    def Deposit_Amount(self, amount): # to add new amount to balance
        if amount > 0:
            self.Amount(amount)
            self.Transaction_Count += 1
            self.Transaction_History.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
            self.Check_balance()
        else:
            print("Invalid deposit amount.")

    def Withdraw_Amount(self, amount):# to subtract the amount from balance
        if amount > self.MAX_WITHDRAW_LIMIT:
            print(f"Maximum withdrawal limit is ₹{self.MAX_WITHDRAW_LIMIT}")
        elif amount > 0 and amount <= self.get_Amount():
            self.Amount(-amount)
            self.Transaction_Count += 1
            self.Transaction_History.append(f"Withdrawn ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")
            self.Check_balance()
        elif amount <= 0:
            print("Invalid withdrawal amount.") # nagative amount for withdraw
        else:
            print("Insufficient balance.") # lower amount in account

    def Show_Transaction_History(self):# To store the transaction histroy using list
        if not self.Transaction_History:
            print("No transactions yet.")
        else:
            print("=====>--- Transaction History ---<=====")
            for i, t in enumerate(self.Transaction_History, 1):
                print(f"{i}. {t}")
            print(f"Total Transactions: {self.Transaction_Count}")


    def Pin_verification(self): #Pin verification to the Transaction operatons
      for _ in range(3):
        pin = input("Enter your ATM PIN: ")
        if self.verify_pin(pin):
          print("PIN Verified Successfully!\n")
          break
        else:
          print("Incorrect PIN.")
      else:
        print("Card Blocked! Too many wrong attempts.")

      return

    @classmethod
    def Bank_Name(cls):# Class method to print same ATM name to all users
        print("""
                 -------------------------------------------
                           Welcome To ABC Bank ATM
                 -------------------------------------------

              """)
    def Transction(self): # Abstract method



        while True:  #Do-while logic
            print("\n-----------------------------")
            print("ATM MENU")
            print("1. Check Balance")
            print("2.Account Details")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Transaction History")
            print("6. Exit")
            print("-----------------------------")

            choice = input("Enter your choice (1-6): ")
             # choice to perfrom Transaction
            if choice == "1":
                self.Pin_verification()
                self.Check_balance()

            elif choice=="2":
                self.Account_detials()

            elif choice == "3":
                self.Pin_verification()
                amount = float(input("Enter amount to deposit: ₹"))
                self.Deposit_Amount(amount)

            elif choice == "4":
                self.Pin_verification()
                amount = float(input("Enter amount to withdraw: ₹"))
                self.Withdraw_Amount(amount)

            elif choice == "5":
                self.Pin_verification()
                self.Show_Transaction_History()

            elif choice == "6":
                valid=input("Do you want to exit (y/n):")
                if valid=="y":
                  print("\nThank you for using ABC Bank ATM.")
                  break
                else:
                  pass

            else:
                print("Invalid choice. Please try again.")


#======================>Main Program<==========================#
if __name__ == "__main__":

    A_T_M.Bank_Name() #Class method calling

    name = input("Enter Account Holder Name: ")
    ac_number = input("Enter Account Number: ")
    balance = float(input("Enter Initial Balance: ₹"))
    pin = input("Set 4-digit ATM PIN: ")

    atm = A_T_M(name, ac_number, balance, pin) #object Creation
    atm.Transction() #calling the Abstract method using child class object
