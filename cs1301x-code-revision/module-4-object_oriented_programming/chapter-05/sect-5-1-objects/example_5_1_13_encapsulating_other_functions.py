class BankAccount:
  #Initialise balance to 0
  def __init__(self, name, balance = 0.0):
    self.log("Account created!")
    self.name = name
    self.balance = balance
    
  def getBalance(self): # Getter for balance
    self.log("Balance checked at " + str(self.balance))
    return self.balance
  
  def deposit(self,amount):
    self.balance += amount
    self.log("+" + str(amount) + ":" + str(self.balance))
  
  def withdraw(self, amount):
    self.balance -= amount
    self.log("-" + str(amount) + ":" + str(self.balance))
  
  def log(self, message): #Logging method
    myLog = open("Log.txt", "a")
    print(message, file = myLog)
    myLog.close()
    
myBankAccount = BankAccount("David Joyner")
myBankAccount.deposit(20.0)
print(myBankAccount.getBalance())
myBankAccount.withdraw(10.0)
print(myBankAccount.getBalance())

# Output is the printed number of myBankAccount.getBalance()
# 20.0
# 10.0
# as well as the creation of Log.txt in which
# Account created!
# +20.0:20.0
# Balance checked at 20.0
# -10.0:10.0
# Balance checked at 10.0

