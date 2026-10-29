class Bankaccount:
  
    def __init__(self,balance=20000):
        self.__balance=balance
    
    def Deposit(self,ammount_diposit,):
        self.ammount_diposit=ammount_diposit
        if(ammount_diposit>0):
            print("₹",self.ammount_diposit ,"ammount is debit in your account")
            print("₹", self.__balance + self.ammount_diposit,"Total ammount in your account")
        else:
            print("invalid ammount")    
    def Withdraw(self,ammount_withdraw):
        self.ammount_withdraw=ammount_withdraw
        if(self.__balance>ammount_withdraw):
            print(self.ammount_withdraw)
            print("₹", self.ammount_withdraw - self.__balance,"available in your account")
        else:
            print("insufficient balance Available balance =",self.__balance)    
c1=Bankaccount()
c1.Deposit(200)
         