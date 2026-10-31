class BankAccount:
    next_bank_account_no=1001
    def __init__(self,name,balance=0):
        if(balance<0):
            raise ValueError("Initial balance cannot be negative")
        self.name=name
        self.account_no=BankAccount.next_bank_account_no
        BankAccount.next_bank_account_no +=1
        self.__balance=balance
        self.transactions=[]
    def deposit(self,ammount):
        if(ammount<0):
            print("Invalid Ammount")
            return
        self.__balance += ammount
        self.transactions.append(f"Deposited :{ammount}")
    def withdraw(self,ammount):
        if(ammount>self.__balance):
            print("Insuficent balance")
            return
        self.__balance -= ammount
        self.transactions.append(f"withdraw :{ammount}")
    def display(self):
        print("Name =",self.name)
        print("Account_no =",self.account_no)
        print("Balance",self.__balance)
    def Transaction_display(self):     
        print("Transactions are =",self.transactions)   
c1=BankAccount("Tanishk")
c1.deposit(5000)
c1.withdraw(2000)
c1.display()
c1.Transaction_display()