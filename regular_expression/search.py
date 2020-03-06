import re
try:
	print("\n--------------direct string match--------------\n")
	res1 = re.search("ban", "bangla")
	res2 = re.search("desh", "bangla")	# not matching

	print("res1: ", res1.group())
	print("res2: ", res2.group())	# in this line there will be error
except Exception as e:
	print(e)

try:
	print("\n--------------\".\" string match--------------\n")
	string_demo = "Bangladesh is my homeland"

	# "." means any letter(with white space).
	# "+" means minimum 1 charecter to max any.
	
	res3 = re.search(".", string_demo)	# "." in first mean any letter at first
	res4 = re.search("B.n", string_demo)	# "B.n". this mean first letter is "B", then any letter and then "n".
	res4_ = re.search("B.+n", string_demo)	# "B.+n" this means start with "B", then any letter, then any letters when find "n" at last.
	res4__ = re.search("B.+?n", string_demo)	# "B.+?n" this means start with "B", then any letter, then any letters. when find first "n" and then stop.
	res5 = re.search("B.n...", string_demo)	
	res6 = re.search("......", string_demo)	# ".....", five "." any five letter from first.
	res7 = re.search("s.a", string_demo)	# not matching

	print("res3: ", res3.group())
	print("res4: ", res4.group())
	print("res4_: ", res4_.group())
	print("res4__: ", res4__.group())
	print("res5: ", res5.group())
	print("res6: ", res6.group())
	print("res7: ", res7.group())	# in this line there will be error. Beacause here is not match.
except Exception as e:
	print(e)

try:
	print("\n--------------\"w\" string match--------------\n")
	string_demo = "Bangladesh is my homeland"

	# "\w" means any letter(without white space).

	res8 = re.search(r"B\w\w", string_demo)	# "B\w\w" means after only 2 letter
	res9 = re.search(r"B\w+h", string_demo)	# "B\w+h" means start with "B"" and end with "h"
	res = re.search(r"i\w\w", string_demo)	# here is error. cuz \w takes only letter.

	print("res8: ", res8.group())
	print("res9: ", res9.group())
except Exception as e:
	print(e)

try:
	print("\n--------------\"d\" string match--------------\n")
	number1 = "my phone number: 01766461990"
	number2 = "my phoen number: 017 66461990"
	id_and_number = "my id is: 5 and number is 01766461990"
	identity = "my id is 17-33434-1"

	# "*" deifine minimum 0 charecter and max any.
	# "+" means minimum 1 charecter to max any.
	# [12345] mean any one charecter form 1, 2, 3, 4, 5

	res10 = re.search(r"\d+", number1)	# \d+ means start with digit and then any number of digit.
	res11 = re.search(r"\d{3}\s*\d{8}", number2)	# \d{3}\s*\d{8} means start with 3 digit, then space could be placed or not, then 8 digit.
	res12 = re.search(r"\d{11}", id_and_number)	# \d{11} means 11 digits togather
	res13 = re.search(r"\d{2}-\d{5}-[123]", identity)	# \d{2}-\d{5}-[123] means 2 digits, then a "-", then 5 digits, then a "-", then one digit between 1 or 2 or 3

	print("res10: ", res10.group())
	print("res11: ", res11.group())
	print("res12: ", res12.group())
	print("res13: ", res13.group())
except Exception as e:
	print(e)