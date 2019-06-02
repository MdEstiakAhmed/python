s="dimik's"
S='dimik\'s'
print(s)
print(S)

#string adding
a="bangla"
b="desh"
print(a+b)
print("")

#string find
#if string isn't available then return -1
#if string is available then return the first letter position
X="bangladesh"
print(X.find("ban"))
print(X.find("desh"))
print(X.find("ben"))
print("")

#string replace
line="this is first line. this is second line."
new_line=line.replace("this","that")
print(line)
print(new_line)

x="helloworld"
x=x.replace("hello","HELLO")
print(x)
print("")

#space remove
text=" this is a string. "
print(text.lstrip())#remove first space
print(text.rstrip())#remove last space
print(text.strip())#remove both first and last space
print(text)
print("")

#upercase and lower case
p="bangladesh"
upper_p=p.upper()
print(upper_p)
lower_p=upper_p.lower()
print(lower_p)
cap_p=p.capitalize()
print(cap_p)
print("")

#split a string
S="I am a student"
list_word=S.split()
print(S)
print(list_word)
print("")

for i in list_word:
	print(i)
print("")

print(list_word[0])
print(list_word[1])
print(list_word[2])
print(list_word[3])
print("")

#count a string
Z="this is a dog. this is a cat"
counter=Z.count("is")
print(counter)
print("")

#check string is start or end with any specific string
Y="bangladesh"
print(Y.startswith("ban"))
print(Y.startswith("Ban"))
print(Y.endswith("desh"))
print(Y.endswith("h"))
