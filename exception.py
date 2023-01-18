def additoin(x, y):  
          x = 10
          y = 20
          print("Addition:", x + b)

try:
      additoin(10, 20)
except NameError:
    print(" b is not define..")

except:
    print("Operation needed to be done if successful")
else:
    print("the operation is successful")