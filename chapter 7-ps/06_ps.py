
#5!=5x3x4x2x1

n=int(input("Enter the number:"))
product=1
for i in range(1,n+1):
    product=product*i
print(f"Factorial of {n} is {product}")