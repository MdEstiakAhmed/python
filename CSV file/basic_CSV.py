import csv
column_name = ["name", "id", "email", "blood group"]
student1 = ["MD estiak ahmed", "17-33434-1", "estiak97@gmail.com", "B+"]
student2 = ["fahim ahmed", "17-33458-1", "fahim011@gmail.com", "A+"]
student3 = ["adnan harun", "19-33433-1", "adnanharun@gmail.com", "A+"]

student_list = [student1, student2, student3]

print(student_list)

# with open("student.csv", "w") as csvf:
#     csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
#     csv_writer.writerow(column_name)
#     for book in student_list:
#         csv_writer.writerow(book)

