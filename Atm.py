dic = {1234567: [1234, 0]}#In the dic having a list values[0]=pin and values[1]=amount

def check_Account(n):
    while True:
        s = 0
        print("Enter the pin: ")
        if int(input()) == dic.get(n)[0]:
            while True:
                print("1. Withdraw Amount")
                print("2. Deposit Amount")
                print("3. Check Balance")
                print("4. Exit")
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    print(Withdraw_Amount(n))
                elif choice == 2:
                    print(deposit_Amount(n))
                elif choice == 3:
                    print(check_Balance(n))
                elif choice == 4:
                    s = 1
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
        else:
            print("Invalid Pin")
            print("1. Enter the pin again?")
            print("2. Exit")
            p = int(input())
            if p == 2:
                return "Thanks for visiting :)"
            else:
                pass
        if s == 1:
            return "Visit again :)"

def Withdraw_Amount(n):
    print("Enter the amount:")
    amt = int(input())
    bal = dic.get(n)[1]
    if bal >= amt:
        bal -= amt
        dic.get(n)[1] = bal
        return f"Your remaining balance is: {bal}"
    else:
        return "Insufficient funds!"

def deposit_Amount(n):
    print("Enter the amount to be deposited:")
    amt = int(input())
    if amt >= 1:
        dic.get(n)[1] = dic.get(n)[1] + amt
        print(f"The amount of {amt} is deposited.")
        return f"The total amount is: {dic.get(n)[1]}"
    else:
        return "Please enter an amount greater than zero."

def check_Balance(n):
    return f"Current Balance: {dic.get(n)[1]}"

while True:
    print("Enter Account No:")
    accountNo = int(input())
    if len(str(accountNo)) >= 6 and accountNo in dic:
        print(check_Account(accountNo))
    else:
        print("Account Number Invalid or Does Not Exist")
