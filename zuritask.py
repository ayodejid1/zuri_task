import cmd
from datetime import date
from datetime import datetime
import random

# today = date.today()
# d1 = today.strftime("%d/%m/%Y")
now = datetime.now()
d2 = now.strftime("%d/%m/%Y %H:%M:%S")

# account
accountDatabase = {}


# program initiation
def init():
    print('Welcome to BankDee1, today is: ', d2 + '**********' * 4)
    print(""""
    (1) Existing Customer
    (2) New Customer
    (3) Account Recovery 
    """ + '**********' * 4)

    userInp = int(input('Select Option: \n'))

    if userInp == 1:

        login()
    elif userInp == 2:

        register()
    elif userInp == 3:

        accountRecovery()
    else:
        print('You have selected an invalid option!')
        init()


"""
login operations begin here -_-
"""


def fmrLogin():
    cmd = input('what is your name? \n')
    customer_name = ['deji', 'seun', 'tunde']
    customer_password = ['deji1', 'seun2', 'tunde3']
    account_balance = [50000, 30000, 100000]
    if cmd in customer_name:
        password = input("input your password? \n")
        customer_id = customer_name.index(cmd)

        if password == customer_password[customer_id]:

            print('Welcome %s' % cmd)
            print("You're logged in successfully!")
            print("today's date is: ", d2)
            print('These are the available options to be selected from: ')
            print("""
           1. Withdrawal
           2. Deposit
           3. Complaint
                   """)
            selected_option = int(input("Please select an option: \n"))
            # WITHDRAWAL
            if selected_option == 1:
                print('You selected %s' % selected_option)
                print('(1) savings \n (2) current\n')

                selected_option = int(input(' Select an option: \n'))

                if selected_option == 1:
                    print('Savings account selected!')
                    amount_to_withdraw = int(input("How much would you like to withdraw? \n"))
                    if amount_to_withdraw <= account_balance[customer_id]:
                        print("Take your cash")
                    else:
                        print("insufficient funds!")
                        exit()

            # DEPOSIT
            elif selected_option == 2:
                print("You selected %s" % selected_option)
                print('(1) savings \n (2) current\n')

                selected_option = int(input(' Select an option: \n'))

                if selected_option == 1:
                    print('Savings account selected!')
                    amount_to_deposit = int(input("How much would you like to deposit? \n"))
                    curr_acc_bal = amount_to_deposit + account_balance[customer_id]
                    if amount_to_deposit > 0:
                        print("Deposit completed!, your current account balance is ", curr_acc_bal)
                        exit()


            # COMPLAINT
            elif selected_option == 3:
                print("You selected %s" % selected_option)
                print('(1) Report a complaint\n (2)Exit \n')

                selected_option = int(input(' Select an option: \n'))
                if selected_option == 1:
                    print('you selected %s' % selected_option)
                    response = input("What issue will you like to report: \n")
                    print("Thank you for contacting us ")
                    exit()
                else:
                    exit()

        else:
            print("Invalid Password!")
    else:
        print("Invalid customer name, try again !")


# login operation
def login():
    print('****** Login ******')

    accountNumberFromUser = int(input('what is your account number?\n'))
    password = input('what is your password \n')

    for accountNumber, userDetails in accountDatabase.items():
        if accountNumber == accountNumberFromUser:

            if userDetails[2] == password:
                bankOperation(userDetails)

#    print('Invalid account or password')
 #   login()


def register():
    print(" ******* Register ******* ")
    email = input("what is your email address?\n")
    first_name = input("what is your first name?\n")
    last_name = input("what is your last name?\n")
    phoneNum = input("your phone number: \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    accountDatabase[accountNumber] = [first_name, last_name, email, phoneNum, password]

    print("Your account has been created!")
    print('== === ==== ==== ===')
    print('your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print(' == === ==== ==== ===')

    login()


def accountRecovery():
    print('----------' * 4 + '\nLost account details\n' + '----------' * 4)
    print('(1) Lost account number\n (2) Forgot Password \n (3)change mobile number \n ' + '**********' * 4)
    userInp = int(input('Select Option: \n'))

    if userInp == 1:
        psChange = input('Enter your email:')
        print('check your phone for a text message received')
    elif userInp == 2:
        psChange = input('Enter your email:')
        print('check your email for confirmation and access to set new password')
    elif userInp == 3:
        confirmationForAccountUpdate()
    else:
        init()


def confirmationForAccountUpdate():
    print('welcome to phone number update')
    idCheck = input('do you have a BVN? \n')
    if idCheck.lower() == 'yes' or idCheck.lower() == 'y':

        while True:
            userInp = input(' enter your bvn number: \n')
            print('Your BVN number is: %s \n Thank you, please check your mail!' % userInp)
            init()
    else:
        print(' Wrong input')
        confirmationForAccountUpdate()


# ---- account  details recovery ends ----

# bank operations
def bankOperation(user):
    print('**********' * 4)
    print('Login is successful')
    print('**********' * 4)
    print('Welcome %s %s ' % (user[0], user[1]))

    print('**********' * 4)

    print('**********' * 4)
    print('what would you like to do: ')
    print('1. Withdrawal')
    print('2. Deposit')
    print('3. Balance')
    print('4. logout')
    selectedOption = int(input('Please select an option: \n'))
    print('**********' * 4)

    if selectedOption == 1:
        withdrawalOperation()
        bankOperation(user)

    elif selectedOption == 2:
        depositOperation()
        bankOperation(user)

    elif selectedOption == 3:
        balanceOperation()
        bankOperation(user)

    elif selectedOption == 4:
        logout()

    else:
        print('invalid option selected')


def balanceOperation():
    accountDatabase.get("currentBalance")
    print('Your balance is N%f \n Deposit Transaction completed' % accountDatabase['currentBalance'])


def depositOperation():
    print("Deposit Operations")
    accountDatabase.get("balance")
    balance = accountDatabase.get("balance")
    amount = float(input("Enter amount: "))
    balance = amount + balance
    accountDatabase["currentBalance"] = balance
    print("Your balance is N %f \nDeposit Transaction Completed" % accountDatabase["currentBalance"])
    print("Reference Number: N", random.randint(10000, 100000))


def withdrawalOperation():
    amount = float(input('Enter Amount: '))

    balance = accountDatabase.get('currentBalance')
    balance = balance - amount
    accountDatabase['currentBalance'] = balance
    print('Take your cash:')
    print(' Withdrawal transaction completed.')
    print('Reference number:', random.randint(10000, 100000))


def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    print('You have successfully logged out!')
    print('Thank you for Banking with us!')
    login()


init()
