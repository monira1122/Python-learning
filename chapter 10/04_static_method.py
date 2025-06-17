class employee:
    language="python"
    salary="12k"

    def getinfo(self):
        print(f"The language is: {self.language} \nThe salary is: {self.salary}" )
    @staticmethod
    def greet():
        print("Good morining")

moni=employee()
moni.language="js"  #This is an instance attribute
print(moni.language,moni.salary)

# employee.getinfo(moni)
moni.getinfo()
moni.greet()