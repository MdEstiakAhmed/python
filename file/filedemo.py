# file create and write rule 1
fp = open("newfile.txt", "w")
fp.write("this file is created using python")
fp.close()

# file create and write rule 2
with open("newfile1.txt", "w") as f:
    f.write("hello python")