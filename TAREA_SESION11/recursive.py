def serie_recursive(n,p):
    if n == 0:
        return 0
    else:
        num_sm = n*p+serie_recursive(n-1,p)
        return num_sm

n = int(input("Ingresa el valor de n: "))
p = int(input("Ingresa el valor de p: "))
print(serie_recursive(n,p))