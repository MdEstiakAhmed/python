import re

try:
	with open("sample3.html", "r") as fp:
		list1 = fp.read()
		# print(list1)
		result = re.findall(r"<li>\n\t\t\t\t(.*?)\n", list1)
		result1 = re.findall(r"<li>(.*?)</li>",list1)
		# print(result)
		# print(result1)
		j = 0
		for i in range(len(result)):
			print(f"\n{result[i]}: {result1[j]}, {result1[j+1]}, {result1[j+2]}")
			j += 3
except Exception as e:
	print(e)

