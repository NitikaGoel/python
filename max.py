nums = input("enter a list of comma separated numbers:")
intlistofnumbers =list(map(int,nums.split(',')))
print(max(intlistofnumbers))
print(max(intlistofnumbers))
setofno = set(intlistofnumbers)
setofno.remove(max(setofno))
print(max(setofno))
print(max(setofno))
print("Second max number is:" +str(max(setofno)))



