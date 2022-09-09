# This program is for developed to make ATM withdrwal process

pin = '1234'
balance = 100

def Widthdraw_Cash():
    withdrawalAmount = int(input('Enter the amount to withdraw, plese enter amount multiple of 10 : '))
    if withdrawalAmount % 10==0:
        if withdrawalAmount <= balance :
            remainingBalance = balance-withdrawalAmount
            print('Your transation is succesful.\nPlese collect your cash')
            print('You have remaining balance:{}'.format(remainingBalance))
            return remainingBalance
        else:
            raise Exception('insufficient balance!')
    else:
        raise Exception("Enter amount in multiple of 10. Try again!")

def InputOption():
    try:
        return int(input('Enter the Option\n\t Enter 1 for withdraw \n\t Enter 2 the balance \n\t Enter anyother number for Quit :'))
    except:
        raise ValueError("Invalid option!")

if __name__ == '__main__':
    pinTotalattempt =0
    allowedPinAttempt = 3
    try:
        for attempt in range(3) :
            userPin = input('Enter your four digit pin :')
            pinTotalattempt+=1
            if pin == userPin:
                option = InputOption()
                if option == 1:
                    balance = Widthdraw_Cash()
                elif option == 2:
                    print("Your Balance is {}".format(balance))
                break
            else:
                print('Wrong pin! please enter correct pin.')
                print('You have only {} attempt left.'.format(allowedPinAttempt-pinTotalattempt))
    except ValueError as v:
        print('Value Error: ', v)
    except Exception as e:
        print('Exception occured: ', e)
    finally:
        print('Logged out successfully!')
