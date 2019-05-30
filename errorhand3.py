def ask():
    while True:
        try:
            no = int(input("Please enter a number :"))
            res = no**2
        except:
            print("Enter input is not a number")
            continue
        else:
            print(res)
            break
        finally:
            print("Execution terminated")

    
        