from __future__ import division
num1 = int(input("Please enter a number :"))
num2 = int(input("Please enter one more number :"))
print("Numbers entered are :" ,num1 , num2)

try:
    print("Integer division of two numbers is " ,int(num1/num2))
    print("Floar division of two numbers is " ,num1/num2)
    print("Floar division of two numbers is " ,num1//num2)
except ZeroDivisionError:
    print("Division by 0 is not allowed")
