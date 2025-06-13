# if elif else ladder

a=int(input("Enter the age:"))
#if statement no: 1

if(a%2==0):
    print("a is even")

#if statement no: 2
if(a>18):
    print("you're above the consent")
    print("Good luck")
elif(a<0):
     print("You are entering invaild age")

elif(a==0):
     print("You are entering wrong age")

else:
     
     print("you're below the consent")   

print("End program")    