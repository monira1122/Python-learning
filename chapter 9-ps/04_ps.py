word="donkey"
with open("file.txt") as f:
     content=f.read()

     contentnew=content.replace(word,"#####")
     with open("file.txt","w") as f:
       f.write(contentnew)