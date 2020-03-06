import re
try:
	res1 = re.search("ban", "bangla")
	res2 = re.search("desh", "bangla")
	print(res1.group())
	print(res2.group())
except Exception as e:
	print(e)