import re

try:
	with open("sample1.txt", "r") as fp:
		list1 = fp.read()
		print(list1)
		result = re.findall(r"^.*$", list1, re.MULTILINE)
		print(result)
except Exception as e:
	print(e)

