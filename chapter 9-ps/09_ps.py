with open("file.txt") as f:
    c1=f.read()

with open("poem.txt") as f:
    c2=f.read()

if(c1==c2):
    print("yes this two file are identical")

else:
    
    print("no this two file are not identical")