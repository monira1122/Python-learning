class employee:
    language="python"
    salary="12k"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("i am creating a object")
    

    def getinfo(self):
        print(f"The language is: {self.language} \nThe salary is: {self.salary}" )
        
    @staticmethod
    def greet():
        print("Good morining")

moni=employee("moni","12k","js")
# moni.language="js"  #This is an instance attribute
print(moni.name,moni.language,moni.salary)

# employee.getinfo(moni)
moni.getinfo()
moni.greet()