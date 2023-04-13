import software
def organization():
    numb=''
    while numb != -8:
        numb=int(input("Indice del pais del pais de busqueda: (Para dejar de ejecutar el codigo digitar -8 )"))
        if 1<=numb<=243:
            software.data(numb)
        elif numb==-8:
            break
        else:
            print('Syntax error')

if __name__=='__main__':
    organization()