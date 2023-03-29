import random 
def numb_bigger(l):
    l.sort(reverse=True)
    print(l[0])
def numbs_prime(n):
    for i in range (2,n):# va a ir desde 2 hasta -1 del final
        if n % i == 0:
            return False
    return True
def numb_value(numbs):
    x=[] 
    for i in numbs:
        if numbs_prime(i)==True:
            x.append(i)            
        else:
            pass
    print(x)
def list_aleatory():    
    list_ale=[]
    for i in range (10):
        x =random.randint(1,50)
        list_ale.append(x)
    print(list_ale)
    numb_bigger(list_ale)
    numb_value(list_ale)
if __name__=="__main__":
    list_aleatory()