import random as rand

def matrices(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num = rand.randint(0,50)
            matriz[i].append(num)
    return matriz


    
def bigger(matriz_a):
    a_x = []
    p_x = []
    a_y = []
    p_y = []
    for i in matriz_a:
        x = max(i)
        y = min(i)
        a_x.append(x)
        p_x.append(i.index(x))
        a_y.append(y)
        p_y.append(i.index(y))
        #i.sort(reverse=True)
        #print(i)
        #i.sort()
        #print(i)
    e = max(a_x)
    d = min(a_y)
    print(f'el numero maximo de la matriz es: {e}, en la posicion: [{a_x.index(e)}][{p_x[a_x.index(e)]}]')
    print(a_x)
    print(p_x)
    print(f'el numero minimo de la matriz es: {d}, en la posicion: [{a_y.index(d)}][{p_y[a_y.index(d)]}]')
    print(a_y)
    print(p_y)
       
def app():
    Filas = int(input('Ingrese el número de filas: '))
    Columnas = int(input('Ingrese el número de Columnas: '))
    matriz = matrices(Filas,Columnas)
    print(matriz)
    bigger(matriz)

if __name__=="__main__":
    app()
    