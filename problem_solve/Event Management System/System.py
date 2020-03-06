import datetime
import sys
from datetime import datetime
if __name__ == "__main__":
    print("Welcome to the event management system\n")

    def menu():
        print("Please enter your desire function:")
        print("Enter 1 fro create a new event")
        print("Enter 2 for create new customer")
        print("Enter 3 for reserve a seat")
        print("Enter 4 for delete reservation")
        print("enter 5 for event summary.")
        print("Enter 6 for exit from the system")
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
            eventsummery()
        if ch == 6:
            exitmenu()

    def createevent():
        print("enter event details:\n")
        eventname = input("enter event name: ")
        totalseat = int(input("total seat: "))
        available = totalseat
        booked = 0
        eventtime = input("enter event date(date format: yyyy-mm-dd): ")

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
            print("event Successfully created")
            res = input("To continue press \"Y\". Neither \"N\": ")
            if res == "Y":
                menu()
            elif res == "N":
                exitmenu()
        except IOError:
            print("File doesn't exist")

    def createcustomer():
        print("Enter customer details:\n")
        name = input("enter customer name: ")
        while True:
            email = input("input customer email: ")
            if "@gmail.com" in email:
                break
            else:
                print("wrong email. please enter again.")
                continue

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
            print("Customer Successfully added")
            res = input("To continue press \"Y\". Neither \"N\": ")
            if res == "Y":
                menu()
            elif res == "N":
                exitmenu()
        except IOError:
            print("File doesn't exist")

    def reserveseat():
        print("reservation process:")

        try:
            while True:
                userid = input("enter user id:")
                flag1 = False
                file = open("customer.txt", "r")
                lines = file.read().splitlines()
                file.close()
                for i in range(len(lines)):
                    line = lines[i]
                    contents = line.split(", ")
                    refnumber = contents[0]
                    if refnumber == userid:
                        flag1 = True
                        break
                if flag1 == False:
                    print("invalid user id")
                    continue
                else:
                    break

            while True:
                eventid = input("enter event id:")
                flag2 = False
                file = open("event.txt", "r")
                lines = file.read().splitlines()
                file.close()
                for i in range(len(lines)):
                    line = lines[i]
                    contents1 = line.split(", ")
                    id = contents1[0]
                    if id == eventid:
                        flag2 = True
                        break
                if flag2 == False:
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
            flag = False
            for i in range(len(lines)):
                line = lines[i]
                content = line.split(" ")

                if userid == content[1] and eventid == content[2]:
                    print("one customer can't reserve more the one seat in same event")
                    flag = True
                    exitmenu()
                    break
                else:
                    flag = False
            if flag == False:
                date1 = "2019-06-02"
                file = open("reservation.txt", "r")
                lines = file.read().splitlines()
                file.close()
                las_lines = lines[-1]
                content = las_lines.split(" ")
                reservedid = int(content[0]) + 1
                file = open("reservation.txt", "a")
                file.write("\n" + str(reservedid) + " " + str(userid) + " " + str(eventid) + " " + str(date1))
                file.close()
                print("successfully reserved")
                res = input("To continue press \"Y\". Neither \"N\": ")
                if res == "Y":
                    menu()
                elif res == "N":
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
                    eventid = content[2]
                    file1 = open("event.txt", "r")
                    lines1 = file1.read().splitlines()
                    file1.close()
                    for i in range(len(lines1)):
                        line1 = lines1[i]
                        content1 = line1.split(", ")
                        ckeventid = content1[0]
                        if ckeventid == eventid:
                            eventtime = content1[5]
                            datetime_obj = datetime.strptime(eventtime, '%Y-%m-%d')
                            today1 = datetime.today()
                            timediff = (datetime_obj - today1)
                            hours = timediff.days * 24
                            if hours >= 24:
                                with open("reservation.txt", "r") as inp:
                                    list1 = inp.readlines()
                                with open("reservation.txt", "w") as outp:
                                    for l in list1:
                                        if l.strip("\n") != line:
                                            outp.write(l)
                                    print("reservation delete")
                                    addeventseat(eventid)
                                    res = input("To continue press \"Y\". Neither \"N\": ")
                                    if res == "Y":
                                        menu()
                                    elif res == "N":
                                        exitmenu()
                                break
                            else:
                                print("time up. you can delete your reservation.")
                                res = input("To continue press \"Y\". Neither \"N\": ")
                                if res == "Y":
                                    menu()
                                elif res == "N":
                                    exitmenu()
                    break
        except IOError:
            print("File doesn't exist2")

    def exitmenu():
        print("thanks for visit.")
        sys.exit()

    def activity():
        temp = input("To continue press \"C\". And to exit press \"E\": ")
        return temp

    def addeventseat(eventid):
        file = open("event.txt", "r")
        lines = file.read().splitlines()
        file.close()
        for i in range(len(lines)):
            line = lines[i]
            content = line.split(", ")
            evntid = content[0]
            if evntid == eventid:
                eventname = content[1]
                totalseat = content[2]
                available = int(content[3]) + 1
                booked = int(content[4]) - 1
                eventtime = content[5]
                newline = evntid + ", " + eventname + ", " + totalseat + ", " + str(
                    available) + ", " + str(booked) + \
                          ", " + eventtime
                file = open("event.txt", "r")
                lines = file.read().splitlines()
                file.close()
                for i in range(len(lines)):
                    line = lines[i]
                    content = line.split(", ")
                    evntid = content[0]
                    if evntid == eventid:
                        with open("event.txt", "r") as inputfile:
                            f = inputfile.read()
                        f = f.replace(line, newline)
                        with open("event.txt", "w") as outputfile:
                            outputfile.write(f)
                        break
                break

    def subtracteventseat(eventid):
        file = open("event.txt", "r")
        lines = file.read().splitlines()
        file.close()
        for i in range(len(lines)):
            line = lines[i]
            content = line.split(", ")
            evntid = content[0]
            if evntid == eventid:
                eventname = content[1]
                totalseat = content[2]
                available = int(content[3]) - 1
                booked = int(content[4]) + 1
                eventtime = content[5]
                newline = evntid + ", " + eventname + ", " + totalseat + ", " + str(
                    available) + ", " + str(booked) + \
                          ", " + eventtime
                file = open("event.txt", "r")
                lines = file.read().splitlines()
                file.close()
                for i in range(len(lines)):
                    line = lines[i]
                    content = line.split(", ")
                    evntid = content[0]
                    if evntid == eventid:
                        with open("event.txt", "r") as inputfile:
                            f = inputfile.read()
                        f = f.replace(line, newline)
                        with open("event.txt", "w") as outputfile:
                            outputfile.write(f)
                        break
                break

    def eventsummery():
        print("event details")
        while True:
            eventid = input("enter event id to show details: ")
            file = open("event.txt", "r")
            lines = file.read().splitlines()
            file.close()
            for i in range(len(lines)):
                line = lines[i]
                content = line.split(", ")
                ckid = content[0]
                if ckid == eventid:
                    print("event details:")
                    eventname = content[1]
                    totalseat = content[2]
                    availableseat = content[3]
                    bookedseat = content[4]
                    eventdate = content[5]
                    print(f"event id: {content[0]}\nevent name: {content[1]}\ntotal seat: {content[2]}\n"
                          f"available seat: {content[3]}\nbooked seat: {content[4]}\nevent date: {content[5]}")
                    break
            res = input("To continue press \"Y\". Neither \"N\": ")
            if res == "Y":
                menu()
            elif res == "N":
                exitmenu()

    def reservationreport(reservedid):
        print("reservation report")
        file = open("reservation.txt", "r")
        lines = file.read().splitlines()
        file.close()
        for i in range(len(lines)):
            line = lines[i]
            content = line.split(" ")
            reserveid = content[0]
            if reservedid == reserveid:
                cusid = content[1]
                file1 = open("customer.txt", "r")
                lines1 = file1.read().splitlines()
                file1.close()
                for i in range(len(lines1)):
                    line1 = lines1[i]
                    content1 = line1.split(", ")
                    customerid = content1[0]
                    if cusid == customerid:
                        print(f"reservation id:{content[0]}\ncustomer id:{content[1]}\ncustomer name: {content1[1]}"
                              f"event id: {content[2]}\nreservation time: {content[3]}")

    menuchoice = menu()
    choiceselect(menuchoice)