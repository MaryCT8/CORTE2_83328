import tarea_12
def valor_iva(dicc):
    price=''
    while price!='salir':
        price=input("¿De que alimento le gustaria saber el iva? (escriba 'salir' para dejar de ejecutar el codigo) ")
        if price=='salir':
            break
        else: 
            valor_t=float(input('Ingrese el valor neto del producto del mercado actual: '))
            valor_iva=dicc[price]*valor_t
            print(f'\nEl valor base del producto "{price}" es: {valor_t-valor_iva}\nEl valor del IVA es: {valor_iva}')
if __name__=="__main__":
    valor_iva(tarea_12.main())