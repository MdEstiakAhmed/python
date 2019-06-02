info={101:"estiak",102:"tanjin",103:"jami"}	#here no serial should maintain

print(type(info))
print(info)
print(info[101])

print("-------------------------------------------------------")

mark={101:{"bangla":75,"english":74}}

print(mark)
print(mark[101])
print(mark[101]["bangla"])

print("-------------------------------------------------------")

mark[102]={"bangla":71,"english":76}
mark[103]={"bangla":74,"english":79}
mark[104]={"bangla":77,"english":78}
print(mark)

print("-------------------------------------------------------")

print(mark.keys())

print("-------------------------------------------------------")

for i in mark:
	print(i,mark[i]["bangla"])

print("-------------------------------------------------------")

for i in mark:
	print(i,mark[i])
