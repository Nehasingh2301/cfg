global allowedPinAttempt
global pinTotalattempt
def Widthdraw_Cash(balance):
    withdrawalAmount = int(input('Enter the amount to withdraw, please enter amount multiple of 10 : '))
    if withdrawalAmount % 10==0:
        if withdrawalAmount <= balance :
            remainingBalance = balance-withdrawalAmount
            print('Your transation is succesful.\nPlese collect your cash')
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

def ValidatePin(userEnteredPin,userActualPin,balance):
    global pinTotalattempt
    pinTotalattempt += 1
    print(userEnteredPin)
    if userEnteredPin == userActualPin:
        balance = Widthdraw_Cash(balance)
        return balance
    else:
        return False

def RunAtm():
    pin = '1234'
    balance = 100
    message = []
    try:
        for attempt in range(3):
            userPin = input('Enter your four digit pin :')
            result = ValidatePin(userPin,pin,balance)
            if(result == False):
                message.append('You have only {} attempt left.'.format(allowedPinAttempt-pinTotalattempt))
            else:
                balance = result
                return "Your Balance: {}".format(balance)
                break
        return message
    except ValueError as v:
        return ('Value Error: ', v)
    except Exception as e:
        return ('Exception occured: ', e)
    finally:
        print('Logged out successfully!')

if __name__ == '__main__':
    allowedPinAttempt = 3
    pinTotalattempt = 0
    message = RunAtm()
    print(message)