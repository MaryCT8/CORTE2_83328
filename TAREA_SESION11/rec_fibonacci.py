def r_fibonacci(n, a = 0, b = 1):
    if n <= 1:
        return a + b
    else:
        c = a + b
        print(c)
        return r_fibonacci(n-1, a = b, b = c)
           
x = int(input("¿Cuantos numeros de la serie fibonacci imprimo?"))      
print(r_fibonacci(x))