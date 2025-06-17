f=open("poem.txt")
c=f.read()
if("twinkle" in c):
    print("The word is present in  c")

else:
    print("The word is not present in  c")

f.close()