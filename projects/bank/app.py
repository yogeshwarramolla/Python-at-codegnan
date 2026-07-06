users = {
    1234:{'name':'yogi','email':'yogeshwaryogi66@gmail.com','balance':1000000,'pass':2345},
    2345:{'name':'chintu','email':'yogi6@gmail.com','balance':1004343,'pass':3345}
         }

#services
def Register(name:str,email:str,intial_deposit:int,password:str):
    print("oh! you can create the account below")

def login(account:int,password:str)->bool:
    if account in users:
        if password== users[account]['pass']:
         return True
    return False

def balance(account:int):
    current_balance=users[account]['balance']
    return current_balance

def withdraw(account:int,withdraw_amount:int):
    current_balance=users[account]['balance']
    #check amount
    if current_balance>=withdraw_amount:
        users[account]['balance']-= withdraw_amount
        return f"{withdraw_amount} withdraw succesful and Current balance is {users[account]['balance']}"
    return "Insufficent Balance"

def deposit(account:int,deposite_amount:int):
    current_balance=users[account]['balance']
    #check amount
    if current_balance>=deposite_amount:
        users[account]['balance']+= deposite_amount
        return f"{deposite_amount} withdraw succesful and Current balance is {users[account]['balance']}"
    return "Amount deposited"
    

def transfer(sender:int,receiver:int,transfer_amount:int):
    if receiver in users:
        current_balance=users[sender]['balance']
        if current_balance>=transfer_amount:
            users[sender]['balance']-=transfer_amount
            users[receiver]['balance']+=transfer_amount
            return f"{transfer_amount} Transfer succesful and Current Balance is {users[sender]['balance']}"
        return "Insufficenint Balance"
    else:
        return " Recivere not found"

def ministatement(account:int):
    return "You can see the ministatement here"

def logout():
    return "Thank you visit , again."

#main
if __name__=="__main__":
    print("welcome to samll large scale bank")
    print("1.Register\n 2.login")
    choice = int(input("Selcet ur choice:"))
    
    #calling Register function
    if choice == 1:
        print("Register in the development phase")

   #calling login function     
    elif choice==2:
        account = int(input("Enter your number"))
        password= int(input("Enter your password:"))
        login_val= login(account=account,password= password)



        while login_val:
            print("The large scale bank services are:")
            print("1.balance\n 2.withdraw\n 3.deposit\n 4.transfer\n 5.Minstatement\n 6.Logout\n")
            choice =int(input("enter ur choice(1-6):"))

            if choice==1:
                #balance function calling
                current_balance=balance(account=account)
                print(f"current balance is :{current_balance}")

            elif choice==2:
                amount=int(input("enter ur withdraw amount:"))
                #call withdraw function
                res= withdraw(account=account,withdraw_amount=amount)
                print(res)

            elif choice==3:
                amount=int(input("Enter ur deposit amount"))
                res=deposit(account=account,deposite_amount=amount)
                print(res)
            elif choice==4:
                receiver_no=int(input("Enter reciever acc number"))
                amount=int(input("Enter the transfer amount"))
                res=transfer(sender=account,receiver=receiver_no,transfer_amount=amount)   
                print(res)
            elif choice==5:
                res=ministatement(account=account)
                print(res)
            elif choice==6:
                res=logout()
                print(res)
                break
            else:
                print("Invalid Choice:Please slect from the 1-6")
                         
                




   
    