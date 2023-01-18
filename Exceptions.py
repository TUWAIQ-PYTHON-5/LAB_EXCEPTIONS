

def additoin(x, y):
          
          print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("The 'b' is unknown variable")
except Exception as error:
    print("There was an error", error.__class__)
else:
    print("the operation is successful")