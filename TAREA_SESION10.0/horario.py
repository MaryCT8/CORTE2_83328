#ALGORITMO HORARIO
def schedule():
    activity = ["CALCULO INTEGRAL", " FISICA MECANICA","PROGRAMACION APLICADA A SISTEMAS MECATRONICOS", "CONSTITUCION Y DEMOCRACIA", "CIRCUITOS DC","CULTURA ECOLOGICA","TALLER DE FISICA"]
    hour = ["7AM-9AM","9AM-11AM","1PM-3PM","7AM-9AM", "11AM-1PM","9AM-11AM","3PM-5PM"]
    coach = ["Acuña Gomez Edwin Julian","Pineda Rey Hernan","Torres Barrera David Nicolás","Sanchez Parra Yurberney","Bohórquez Ávila Roberto","Sanchez Parra Yurberney","Dora Mora Paula Andrea"]
    day = ["MARTES,JUEVES", "MARTES,JUEVES", "MARTES,JUEVES", "MIERCOLES","MIERCOLES, VIERNES", "VIERNES","VIERNES"]
    class_room=["407 DB","405 DB","303 GO","405 DB","306 DB","306 PS","204 PS"]
    data = input("Ingresa el dato que quieres buscar: ")
    a = activity.index(data)
    print (day[a])
    print (activity[a])
    print (hour[a])
    print (coach[a])
    print (class_room[a])
if __name__=="__main__":
    schedule()