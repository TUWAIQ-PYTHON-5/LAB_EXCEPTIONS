def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError:
    print("Please provide the correct varible name to do the addition process")
except Exception:
    print("There is an error")
else:
    print("the operation is successful")