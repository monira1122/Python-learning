with open("long.txt") as f:
    lines=f.readlines()

    lineno=1
    for line in lines:

        if("python" in line):
         print(f"Yes python in line,line no:{lineno}")
         break
         lineno+=1
    else:
         print("no python not in line")