'''
there is a list. make a new list which is exactly triple of older list.
'''

li=[5,6,7,2,3]
new_li=[(3*x) for x in li]	#run a loop and take every element of li in x. then multiple x by 3 and save in new_li.
print(new_li)

'''
take only even numbers from a list and make a new list.
'''

li=[22,1,5,8,4,56,9]
new_li=[x for x in li if x%2==0]
print(new_li)
