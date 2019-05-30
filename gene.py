import random


def gen1(n1,n2,n3):
    for x in range(n3):
      yield(random.randint(n1,n2))
    

for x in gen1(1,10,3):
    print(x)



s=iter("Hello")
print(next(s))
dir