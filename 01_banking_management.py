#banking management system
'''
1.deposit
2.withdrawl
3.balance check
4.Exit



'''
import time
pin=1225
balance=5000
for i in range(1,4):
    userpin=int(input("Enter your 4 digit pin: "))
    if(userpin==pin):
        print("="*40)
        print(f"{"🏦Welcome to krutika's bannk💕":^50}")
        time.sleep(1)
        print("="*40)
        print("""        1.Deposit
        2. withdraw
        3. Balance Check
        4. Exit
        """)
        while True:
            choice=int(input("Enter your choice (1-4): "))
            if(choice==1):
                deposit=float(input("Enter the amount to be deposited: "))
                balance+=deposit
                if deposit > 0:
                    print(f"Rs {deposit} has been deposited succefully and \n your total balance is {balance}")
                else:
                    print("Invalid credentials")
            

            elif(choice==2):
                withdrawl=int(input("Enter the amount to be withdrawl "))
                if (withdrawl <=balance):
                    balance-=withdrawl #balance-=withdraw (balance mdhun withdraw kra aaniwithdraw la asign kra)
                    print(f"debited amount : -{withdrawl} ur total balance is {balance}")
                else:
                    print("Insufficient balance")
                

            elif(choice==3):
                print(f"Total Balance is: {balance}")
                

            elif(choice==4):
                print("Thanku!!🖤\nHave a nice day🤞")
                break
            else:
                print("Invalid Credential")
        break
    else:
        print("Invalid pin...❌") 
else:
    print("too many wrong attempt! your account is blocked🥶")