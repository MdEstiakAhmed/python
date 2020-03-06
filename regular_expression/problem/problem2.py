import re

try:
	with open("sample2.html", "r") as fp:
		list1 = fp.read()
		print(list1)
		result = re.findall(r"<li>(.*?)</li>", list1)
		print(result)
except Exception as e:
	print(e)

