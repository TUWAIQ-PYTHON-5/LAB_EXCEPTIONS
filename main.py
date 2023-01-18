def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    additoin(10, 20)
except ValueError:
    print("Value Error Check The Function")
except Exception as e:
    print('The Error is : ',e)
else:
    print("the operation is successful")
finally:
    print('This Finally will work even try does not work')
