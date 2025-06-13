marks1=int(input("Enter the mark:"))
marks2=int(input("Enter the mark:"))
marks3=int(input("Enter the mark:"))

total_percentage=(100*(marks1+marks2+marks3))/300

if(total_percentage>40 and marks1>33 and marks2>33 and marks3>33):
    print("you are passed",total_percentage)

else:
    print("you're failed",total_percentage)