number=input("enter your exam number")
number=int(number)
if number>=80:
    grade="A+"
elif number>=75:
    grade="A"
elif number>=70:
    grade="B+"
elif number>=65:
    grade="B"
elif number>=60:
    grade="C+"
elif number>=55:
    grade="C"
elif number>=50:
    grade="D"
else:
    grade="F"

print("your grade is=",grade)
