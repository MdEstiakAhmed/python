import re

try:
	print("\n--------------find string with given pattern--------------\n")

	phone_numbers = "numbers: 01715913448, 01766461990, 01147852334, 00000000000, 01253658, 01937653004"

	result = re.findall(r"01[3456789]\s*\d{8}", phone_numbers)
	print("result: ", result)
except Exception as e:
	print(e)

try:
	print("\n--------------find string with given pattern--------------\n")

	string = "bangla english Bangla"

	# ^ means at first
	# $ means at last

	result1 = re.findall(r"english", string)	# find english is present or not
	result2 = re.findall(r"^english", string)	# find english is present at first or not
	result3 = re.findall(r"english$", string)	# find english is present at last or not
	result4 = re.findall(r"^bangla", string)	# find bangla is present at first or not
	result5 = re.findall(r"bangla$", string)	# find bangla is present at last or not
	result6 = re.findall(r"bangla$", string, re.IGNORECASE)	# find bangla is present at last or not with ignore case
	result7 = re.findall(r"bangla$", string, re.I)	# find bangla is present at last or not with ignore case

	print("result1: ", result1)
	print("result2: ", result2)
	print("result3: ", result3)
	print("result4: ", result4)
	print("result5: ", result5)
	print("result6: ", result6)
	print("result7: ", result7)
except Exception as e:
	print(e)