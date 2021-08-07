print("ALLAH")


class Jazzcash(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.pin = 1234

    def sendmoney(self):
        while True:
            print("1:To Mobile Account")
            print("2: To CNIC")
            print("3: To Bank account")
            print("00: Back Main menu")
            sendmoneyinput = int(input("select one option "))
            print()
            if sendmoneyinput==1:
                while True:
                    print("1:To JazzCash")
                    print("2:EasyPaisa")
                    print("3:Upaisa")
                    print("00:Main Menu")
                    selectpaymentmethod = int(input("select one method "))
                    print()
                    if selectpaymentmethod==1:
                        print()
                        jazzcashnumber = int(input("Enter receiver Jazzcash account number "))
                        if jazzcashnumber==123456789:
                            userpin = int(input("enter 4 digit pin "))
                            if userpin==self.pin:
                                print("Your money has been sent ")
                                break
                        else:
                            print("Please enter correct number")
                    if selectpaymentmethod ==2:
                        print()
                        EasyPaisanumber = int(input("Enter your EasyPaisa account number"))
                        if EasyPaisanumber == 987654321:
                            userpin = int(input("enter your 4 digit pin "))
                            if userpin == self.pin:
                                print("Your easypaisa money has been sent ")
                                break
                    if selectpaymentmethod == 3:
                        print()
                        upaisa = int(input("Enter your EasyPaisa account number"))
                        if upaisa == 987654321:
                            userpin = int(input("enter your 4 digit pin "))
                            if userpin == self.pin:
                                print("Your Upaisa money has been sent ")
                                break

                    if selectpaymentmethod==00:
                        break
            if sendmoneyinput==2:
                receivernumber = int(input("Enter receiver 13 digit Cnic number "))
                cninpin = int(input("Enter CNIC 4 digit pin "))
                if cninpin == self.pin:
                    print("Your Money has been sent on CNIN number ")
            if sendmoneyinput ==3:
                bankaccount = int(input("Enter receiver bank account number  "))
                bankpin = int(input("Enter 4 digit bank pin "))
                if bankpin == self.pin:
                    print("Your money has been sent on bank account ")
            if sendmoneyinput==00:
                break

    def paybills(self):

        print("1:MAPCO")
        print("2:LASCO")
        print("3:FASCO")
        print("00: Back")
        paybillsinput = int(input("Select one option "))
        print()
        while True:
            if paybillsinput==00:
                break
            if paybillsinput==1:
                billrefrencenum = input("enter your 14 digit  bill reference number ")
                if len(billrefrencenum)==14:
                    print("Your Total Bill is RS 2000")
                    paybillpin = int(input("enter pin "))
                    if paybillpin == self.pin:
                        print("Your bill has been depostie")
                        print()
                        break

                else:
                    print("Please enter 14 digit number  ")
            if paybillsinput==2:
                billrefrencenum = input("enter your 14 digit  bill reference number ")
                if len(billrefrencenum)==14:
                    print("Your Total Bill is RS 1120")
                    paybillpin = int(input("enter pin "))

                    if paybillpin == self.pin:
                        print("Your bill has been Deposit")
                        print()
                        break

                else:
                    print("Please enter 14 digit number  ")


    def MobileLoadAndBundles(self):

        print("1: Jazz/Warid load")
        print("2: Telenor load")
        print("3: Ufone Load")
        print("4:Jazz Bundles")
        print("5:Telenor Bundles")
        print("00:Back")
        print()

        while True:
            mobileloadUserInput = int(input("Select one option "))
            print()

            if mobileloadUserInput == 00:
                break

            if mobileloadUserInput == 1:
                EnterJazzWaridNum = int(input("Enter jazz/Warid number "))
                enteramount = int(input("Enter amount "))
                enterpin = int(input("Enter 4 Digit pin "))

                print(f"Your load amount {enteramount} is sent to {EnterJazzWaridNum}")

                break



            if mobileloadUserInput==2:
                EnterJazzWaridNum = int(input("Enter Telenor number "))
                enteramount = int(input("Enter amount "))
                enterpin = int(input("Enter 4 Digit pin "))

                print(f"Your load amount {enteramount} is sent to {EnterJazzWaridNum}")

                break


            if mobileloadUserInput==3:
                EnterJazzWaridNum = int(input("Enter Ufone number "))
                enteramount = int(input("Enter amount "))
                enterpin = int(input("Enter 4 Digit pin "))

                print(f"Your load amount {enteramount} is sent to {EnterJazzWaridNum}")

                break

            if mobileloadUserInput==4:
                EnterJazzWaridNum = int(input("Enter jazz/Warid number "))
                enteramount = int(input("Enter amount "))
                enterpin = int(input("Enter 4 Digit pin "))

                print(f"Your load amount {enteramount} is sent to {EnterJazzWaridNum}")

                break

            if mobileloadUserInput==5:
                EnterJazzWaridNum = int(input("Enter jazz/Warid number "))
                enteramount = int(input("Enter amount "))
                enterpin = int(input("Enter 4 Digit pin "))

                print(f"Your load amount {enteramount} is sent to {EnterJazzWaridNum}")

                break








try:
    username = input("enter your name ")
    password = int(input("enter your password "))
    obj = Jazzcash(username, password)



    if username == "a" and password== 1:

        while True:

            print("1 : send Money")
            print("2 : Pay Bills ")
            print("3 : Mobile Load and Bundles")
            print("4 : Ready JazzCash")
            print("5 : quit")
            userinput = int(input("select option "))
            print()

            if userinput==5:
                print("Thank You for using JazzCash by")
                break
            if userinput==1:
                obj.sendmoney()

            if userinput==2:
                obj.paybills()


            if userinput==3:
                obj.MobileLoadAndBundles()



    else:
        print("enter correct name ad password ")
except:
    print(f"try again")