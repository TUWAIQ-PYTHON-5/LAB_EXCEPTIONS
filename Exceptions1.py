def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)

    
try:
    additoin(10, 20)
except NameError:
    print("try again")

except:
   print (" something went wrong , try again")

else:
   print ("the opertion is successful")

