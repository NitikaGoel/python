import errorhand3
try:
    x=5
    y=0
    z=x/y
except ZeroDivisionError:
    print("Divion by zero is not allowed")
finally:
    print("Execution completed")

errorhand3.ask()