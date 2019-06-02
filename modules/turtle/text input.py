import turtle
n=int(input("input public number:"))
i=0
while 1:
        if i==n:
                break
                
        name=turtle.textinput("name","what is your name?")
        name=name.lower()

        if name.startswith("mrs") or name.startswith("ms"):
                print("hello madam, how are you?")

        elif name.startswith("mr"):
                print("hello sir, how are you?")

        else:
                name=name.capitalize()
                STR="hi "+name+","+"how are you?"
                print(STR)
        i+=1
turtle.exitonclick()
