s1={1,2,3,4,5}
s2={2,4,6,8}

a=s1 & s2	# A intersection B (common things)
b=s1 | s2	# A union B (all things)
c=s1 ^ s2	# A bar B (all things except common thtings)
d=s1 - s2	# A - B (available in A but not in B)

print(a)
print(b)
print(c)
print(d)