class student:
    def __init__(self):
        self.name=input("Enter the name of the student :")
        self.id=int(input("Enter the id :"))
        self.marks=[]
        print("Enter Marks in 5 Subjects ")
        for i in range(5):
            x=int(input(f"Enter the {i+1} mark :"))
            self.marks.append(x)
        self.total=sum(self.marks)
        self.avg=self.total/5
    def display(self):
        print("---Student Details---")
        print(f"Name : {self.name}")
        print(f"ID : {self.id}")
        print("Marks Obtained in 5 Subjects")
        for i in range(5):
            print(f"{i+1} Subject marks is : {self.marks[i]}")
        print(f"Total Mark : {self.total}")
        print(f"Average is : {(self.avg)}")
    @classmethod
    def top(cls,stu,n): 
        high=0
        name=''  
        for i in range(n):
            if stu[i].total>high:
                high=stu[i].total
                name=stu[i].name
        print(f"The Student with Hgihest mark Name : {name} marks obtained : {high}")
n=int(input("Enter Number of Students :"))
x=[i for i in range(n)]
for i in range(n):
    x[i]=student()
student.top(x,n)




    