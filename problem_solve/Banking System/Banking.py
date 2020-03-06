print("Welcome to the system")

# function that dispalys menu and returns user selected choice
def displayMenu():
    print("Please choose the functionality:")
    print("1)Add new customer")
    print("2)Perform deposit transaction")
    print("3)Perform withdrawal")
    print("4)View current balance")
    print("5)View transaction history")
    print("6)Exit")
    ch=int(input("Enter your choice[1/2/3/4/5/6]: "))
    return ch

#call the function as per user selected choice
def executeMenuChoice(ch):
    if(ch==1):
        addCustomer()
    elif(ch==2):
        deposit()    
    elif(ch==3):
        withdrawal()
    elif(ch==4):
        diaplayCurrentBalance()
    elif(ch==5):
        diaplayTransactions()      
    elif(ch==6):
        exit()
    else:
        print("Invalid oprion...")
        displayMenu()

def addCustomer():
    print("Provide details of the customer without space:")
    fName=raw_input("First name: ")
    lName=raw_input("Last name: ")
    contactNo=raw_input("Contact Number: ")
    balance=raw_input("Opening Balance: ")
    try:
        file = open("Customers.txt","r")
        lines = file.read().splitlines()        
        las_lines=lines[-1]
        content=las_lines.split()        
        acctNumber=int(content[0])+1
        custNumber=int(content[3])+1
        file.close()
        file = open("Customers.txt","a")
        
        file.write("\n"+str(acctNumber)+" "+fName+" "+lName+" "+str(custNumber)+" "+contactNo+" "+str(balance))
        file.close()
        print("Customer Successfully added......")
    except IOError:
        print("File doesn't exist")
    except TypeError:
        print("performing arithmetic operation on no numeric data")

def accountExist(accNumber):
    try:
        file = open("Customers.txt","r")
        for line in file:
            content = line.split()   
            if(accNumber==int(content[0])):            
                file.close()
                return True,int(content[5])
        
    except IOError:
        print("File doesn't exist")
    file.close()
    return False,0

def deposit():
    accNum=input("Enter Account Number: ")
    accExist, currentBalance=accountExist(accNum)
    print(accExist)
    if(accExist==True):
        amount=input("Enter amount to deposit: ")
        date=raw_input("Enter date of transaction(dd/mm/yyyy): ")
        currentBalance=currentBalance+amount
        newLine=""
        try:
            file = open("Customers.txt","r")
            lines = file.read().splitlines()
            lastLinesNo=len(lines)
            currentLine=1
            for line in lines:
                content = line.split()
                if(currentLine!=lastLinesNo):
                    if(accNum==int(content[0])):
                        newLine+=content[0]+" "+content[1]+" "+content[2]+" "+content[3]+" "+content[4]+" "+str(currentBalance)+"\n"
                    else:
                        newLine+=content[0]+" "+content[1]+" "+content[2]+" "+content[3]+" "+content[4]+" "+content[5]+"\n"
                else:
                    if(accNum==int(content[0])):
                        newLine+=content[0]+" "+content[1]+" "+content[2]+" "+content[3]+" "+content[4]+" "+str(currentBalance)
                    else:
                        newLine+=content[0]+" "+content[1]+" "+content[2]+" "+content[3]+" "+content[4]+" "+content[5]
                currentLine=currentLine+1
            file.close()
        except IOError:
            print("File doesn't exist")
        file = open("Customers.txt","w")
        file.write(newLine)
        
        file=open("Transactions.txt","a")
        file.write("\n"+str(accNum)+" "+date+" "+"Deposit"+" "+str(amount))
        file.close()
    else:
        print("Invalid Account number/account doen't exist, try again")
        deposit()

def withdrawal():
    print("implement logic here")

def diaplayCurrentBalance():
    print("implement logic here")

def diaplayTransactions():
    print("implement logic here")
    
ch=displayMenu()
executeMenuChoice(ch)
