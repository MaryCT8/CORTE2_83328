import random

def aleatory():
    n = 1
    
    while n<=10:
        x = random.randint(100,120)
        if x == 110 or x == 115 or x == 119:
            pass
        elif x % 2 == 0:
            print(x)
            n += 1
            while n<=10:
                i = random.randint(100,120)
                if x == 110 or x == 115 or x == 119:
                   pass
                elif i % 2 == 1:
                    print(i)
                    n += 1
                    break
print(aleatory())