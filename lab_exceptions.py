 
try:
    def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)


    additoin(10, 20)
except NameError as error:
     print("Name b is not defined",error.__class__)
except IndentationError as error:
     print("Unexpected indent",error.__class__)
else:
      print("the operation is successful")

     
