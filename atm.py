class Atm (object):
    def __init__(self,card_no,pin):
        self.card_no=card_no
        self.pin=pin
        
    def balance (self):
     print("your balance is 50,000")
    def withdraw(self,amount):
        new=50000-amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new))

def main ():
    Card_number = input("insert your card number:- ") 
    pin_number = input("enter your pin number:- ")
    new_user = Atm(Card_number ,pin_number)
    print("chose activity")
    print("1 balance , 2 withdraw")
    activity = int(input("enter activity number :- "))
    if (activity == 1):
        new_user.check_balance() 
    elif (activity == 2): 
        amount = int(input("enter the amount:- "))
        new_user.withdraw(amount) 
    else: print("enter a valid number")
if __name__ == "__main__": 
    main()