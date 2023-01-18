

def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError :
        print("you try to use a variable dose not exist ")
    except Exception as error:
        print("Somthing Wrong !! :  " , error.__class__)
    else:
        print("the operation is successful")     
additoin(10, 20)           




