with open("old.txt") as f:
    c=f.read()

with open("reanmed_by_python","w") as f:
    f.write(c)