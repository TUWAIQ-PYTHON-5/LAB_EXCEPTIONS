
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try :  
 additoin(10, 20)
except IndentationError:
    print("please check the Improper indentation")
except NameError: 
        print("please check variables again ")
except :
        print("something went wrong , please try again !! ")
else :
    print("the operation is successful")