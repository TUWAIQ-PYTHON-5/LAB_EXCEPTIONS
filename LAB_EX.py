

def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + y)


try :
    additoin(10, 20)


except NameError as error :

    print (" The Name ", error.name , " is not defind ")

except :
    
      print (" Addition :" , additoin , "the operation is successful")
  

