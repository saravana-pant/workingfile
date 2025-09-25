class student:
    def input1(self):
        self._name=input("Enter the Name of the Student : ")
        self._id=int(input("Enter the id of the Student : "))
    def display(self):
        print(f"Name : {self._name}")
        print(f"ID : {self._id}")
class test(student):
    def input(self):
        self.input1()
        self._marks=[]
        print("Enter 5 Subject marks : ")
        for i in range(5):
            x=int(input(f"Subject {i+1} : "))
            self._marks.append(x)
    def display(self):
        super().display()
        print("Marks Obtained in 5 Subjects")
        for i in range(5):
            print(f"Mark Obtained in {i+1} Subject is : {self._marks[i]}")
class result(test):
    def __init__(self):
        self.input()
        self.total=sum(self._marks)
        self.avg=self.total/5
    def display(self):
        super().display()
        print(f"Marks is : {self.total}")
        print(f"Average is : {self.avg}")
stud=[]
n=int(input("Enter Number of Students : "))
for i in range(n):
    print(f"Enter the {i+1} Student Details : ")
    x=result()
    stud.append(x)
print("Students details are!!\n")
for i in range(n):
    print("\n")
    print(f"Student {i+1} Details!")
    stud[i].display()
