import datetime

if __name__ == "__main__":
    print("Welcome to the event management system\n")

    customerinfo = {}

    def menu():
        print("Please enter your desire function:")
        print("Enter 1 fro create a new event")
        print("Enter 2 for create new customer")
        print("Enter 3 for reserve a seat")
        print("Enter 4 for delete reservation")
        print("Enter 5 for exit from the system")
        choice = int(input("Enter your choice[1/2/3/4/5/6]: "))
        return choice

    def choiceselect(ch):
        if ch == 1:
            createevent()
        if ch == 2:
            createcustomer()
        if ch == 3:
            reserveseat()
        if ch == 4:
            deletereserve()
        if ch == 5:
            exitmenu()

    def createevent():
        print("enter event details:\n")
        eventname = input("enter event name:")
        totalseat = int(input("total seat:"))
        available = totalseat
        booked = 0
        eventtime = input("enter event date(date format: yyyy-mm-dd):")

        try:
            file = open("event.txt", "r")
            lines = file.read().splitlines()
            las_lines = lines[-1]
            content = las_lines.split(",")
            eventid = int(content[0]) + 1
            file.close()
            file = open("event.txt", "a")

            file.write("\n" + str(eventid) + ", " + eventname + ", " + str(totalseat) + ", " + str(available) + ", " + str(booked)
                       + ", " + str(eventtime))
            file.close()
            print("Customer Successfully added......")
        except IOError:
            print("File doesn't exist")

    def createcustomer():
        referenceid = 1000
        info = {}
        cus = {}
        print("Enter customer details:\n")
        refid = referenceid
        referenceid += 1
        name = input("enter customer name: ")
        email = input("input customer email: ")
        # while True:
        #     email = input("input customer email: ")
        #     if email == "estiak97@gmail.com":
        #         break
        #     else:
        #         print("wrong email. please enter again.")
        #         continue
        # info[refid] = {"name": name, "email": email}
        # customerinfo.update(info)

        try:
            file = open("customer.txt", "r")
            lines = file.read().splitlines()
            las_lines = lines[-1]
            content = las_lines.split(",")
            refnumber = int(content[0]) + 1
            file.close()
            file = open("customer.txt", "a")

            file.write("\n" + str(refnumber) + ", " + name + ", " + email)
            file.close()
            print("Customer Successfully added......")
        except IOError:
            print("File doesn't exist")

        # temp = activity()
        # if temp == "C":
        #     menu()
        # elif temp == "E":
        #     exitmenu()
        # else:
        #     print("wrong input. click again")
        #     activity()

    def reserveseat():
        print("reservation process:")

        try:
            while True:
                userid = input("enter user id:")
                flag = False
                file = open("customer.txt", "r")
                lines = file.read().splitlines()
                file.close()
                for i in range(len(lines)):
                    line = lines[i]
                    content = line.split(",")
                    refnumber = content[0]
                    if refnumber == userid:
                        flag = True
                        break
                if flag == False:
                    print("invalid user id")
                    continue
                else:
                    break

            while True:
                eventid = input("enter event id:")
                flag = False
                file = open("event.txt", "r")
                lines = file.read().splitlines()
                file.close()
                for i in range(len(lines)):
                    line = lines[i]
                    content = line.split(",")
                    id = content[0]
                    if id == eventid:
                        flag = True
                        break
                if flag == False:
                    print("invalid event id")
                    continue
                else:
                    break
        except IOError:
            print("File doesn't exist1")

        try:
            file = open("reservation.txt", "r")
            lines = file.read().splitlines()
            file.close()
            for i in range(len(lines)):
                line = lines[i]
                content = line.split(" ")
                cusid = content[1]
                evntid = content[2]
                flag = False
                if cusid == userid and evntid == eventid:
                    print("one customer can't reserve more the one seat in same event")
                    flag = True
                    exitmenu()
                    break
                else:
                    flag = False
            if flag == False:
                date = datetime.date.today()
                file = open("reservation.txt", "r")
                lines = file.read().splitlines()
                file.close()
                las_lines = lines[-1]
                content = las_lines.split(" ")
                reservedid = int(content[0]) + 1
                file = open("reservation.txt", "a")
                file.write("\n" + str(reservedid) + " " + str(userid) + " " + str(eventid) + " " + str(date))
                file.close()
                print("successfully reserved")
                exitmenu()
        except IOError:
            print("File doesn't exist2")

    def deletereserve():
        print("delete reservation:")
        try:
            reserveid = input("enter your reserve number: ")
            file = open("reservation.txt", "r")
            lines = file.read().splitlines()
            file.close()
            for i in range(len(lines)):
                line = lines[i]
                content = line.split(" ")
                rid = content[0]
                if rid == reserveid:
                    with open("reservation.txt", "r") as inp:
                        list1 = inp.readlines()
                    with open("reservation.txt", "w") as outp:
                        for l in list1:
                            if l.strip("\n") != line:
                                outp.write(l)
                        print("reservation delete")
                    break
        except IOError:
            print("File doesn't exist2")

    def exitmenu():
        print("thanks for visit.")

    def activity():
        temp = input("To continue press \"C\". And to exit press \"E\": ")
        return temp

    menuchoice = menu()
    choiceselect(menuchoice)
    for i in customerinfo:
        print(i, customerinfo[i])


