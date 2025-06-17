f=open("file.txt")
print(f.read())
f.close()

#same as
with open("file.txt") as f:
    print(f.read())
