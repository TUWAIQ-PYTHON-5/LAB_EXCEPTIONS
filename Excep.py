def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError:
    print("variables names not defined")

except Exception as error:
    print("the Exception is:", error.__class__)
else:
    print("the operation is successful")

