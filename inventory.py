class invent1:
    def __init__(self):
        self.code=int(input("Enter the Stock Code : "))
        self.no=int(input("Enter Number of Stock : "))
        self.price=int(input("Enter the Price : "))
    def display(self):
        print(f"Code : {self.code}")
        print(f"No : {self.no}")
        print(f"Price : {self.price}")
class invent2:
    def __init__(self,x):
        self.code=x.code
        self.total=x.no*x.price
    def display(self):
        print(f"Total : {self.total}")
        return self.total
n=int(input("Enter Number of Stock : "))
stock=[]
stock1=[]
for i in range(n):
    print(f"Enter the {i+1} Stock Details !")
    x=invent1()
    y=invent2(x)
    stock.append(x)
    stock1.append(y)
total=0
print("Stock Details are!!!")
for i in range(n):
    print(f"Stock {i+1} Details !")
    stock[i].display()
    x=stock1[i].display()
    total+=x
print("Total Stock Selling Price : ",total)



