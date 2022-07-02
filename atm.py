class Atm:
    def __init__(self,cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your Balance is $1500")
    
    def money_withdrawal(self,amount):       
        new_amount = 1500 - amount
        print("Withdrawn Amount is $" + str(amount) )
        print("Remaining Balance left is $" + str(new_amount))
 

def main():
        card_number = input("Enter the Card No : ")
        pin_number = input("Enter you pin number :")
        
        line_spacing = Atm(card_number, pin_number)

        print("1.balance equiry   2.withdrawal")
        selection = int(input("Enter the Option number :"))
        
        if(selection == 1):
            line_spacing.check_balance()
        
        elif(selection == 2):
            amount = int(input("Enter the amount u want :"))
            line_spacing.money_withdrawal(amount)
        
        else:
            print("Please enter a valid option")    
       
if __name__ == "__main__":
     main()   


