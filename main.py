def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)


try:
    additoin(10, 20)
except NameError:
    print("you try to use a variable dose not exist" )
except Exception as error:
    print("error" , error.__class__)    
else:
    print("the operation is successful")    