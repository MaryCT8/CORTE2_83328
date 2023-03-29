import list_al
import horario

print("1) Realice un programa donde se pueda consultar su horario de clases, de modo que ingresando el nombre de la materia indique el día de clase, la hora, el salón y el nombre del profesor.")
print("2) Realice un programa donde permita crear una lista de 10 números aleatorios entre 1 y 50")

opc=input("Ingresa el ejercio que quieres ejcutar: ")
if opc == "1":
    horario.schedule()
elif opc == "2":
    list_al.list_aleatory()
else:
    print("INPUT ERROR")
