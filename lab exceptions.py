 
try:
      def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)


      additoin(10, 20)

except NameError as error:
    print("there is an error", error)

else:
    print("the operation is successful")

