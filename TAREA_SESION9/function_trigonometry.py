import math as m
def calc_op(op,numb):
    if op == 1:
        a = m.sin(rand(numb))
        print(a)
    elif op == 2:
        b = m.cos(rand(numb))
        print(b)
    elif op == 3:
        c = m.tan(rand(numb))
        print(c)
    elif op == 4:
        d = m.exp(numb)
        print(d)
    elif op == 5:
        e = m.log(numb)
        print(e)
    else:
        print("input error")

def rand(x):
    r=x*m.pi/180
    return r

numb=float(input("Ingrese el numero para calcular \n 1.seno \n 2.coseno \n 3.tangente \n 4.exponencial \n 5. logaritmo \n"))
op=int(input("Ingresa la operacion a ejecutar: "))
calc_op(op,numb)



