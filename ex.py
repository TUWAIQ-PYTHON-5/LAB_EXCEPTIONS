
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
try:
    print(input("add the values:"))
    additoin(10, 20)
except NameError as error:
    print("the type of erorr",error.__class__)
except:
    print("the char of Addition is not avilble")
else:
    print("the operation is successful")
