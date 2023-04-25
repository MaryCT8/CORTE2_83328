class Ciudadano:
    def __init__(self):
        self.__name=None
        self.__semester=None
        self.__university=None

#Getters
    def getName(self):
        return self.__name
    def getSemester(self):
        return self.__semester
    def getUniversity(self):
        return self.__university
    
 #Setters
    def setName(self,name:str):
        self.__name=name
    def setSemester(self,semester:int):
        self.__semester=semester
    def setUniversity(self,university:str):
        self.__university=university

#Sobrecarga
    def phrase(self):
        return "Action reaction"
        
        
        
class Ing_Multimedia(Ciudadano):
    def __init__(self):
        super().__init__()
        #MATERIA FAV
        self.__imu=None
        #APP FAV
        self.__app=None
    
    def setImu(self,imu:str):
        self.__imu=imu
    
    def getImu(self):
        return self.__imu
    
    def setApp(self,app:str):
        self.__app=app
    
    def getApp(self):
        return self.__app
    
  
    def xd(self):
        return "Me encanta diseñar"
    

class Ing_Quimica(Ciudadano):
    def __init__(self):
        super().__init__()
        #MEZCLA FAV
        self.__qui=None
        #COMPUESTO FAV
        self.__compound=None
    
    def setQui(self,qui:str):
        self.__qui=qui
    
    def getQui(self):
        return self.__qui
    
    def setCompound(self,compound:str):
        self.__compound=compound
    
    def getCompound(self):
        return self.__compound
    
    def phrase(self):
        return "Anyone who says alcohol is not a solution knows nothing about chemistry"
    
class Ing_Mecatronica(Ciudadano):
    def __init__(self):
        super().__init__()
        #APP FAV PARA PROGRAMAR
        self.__imec=None
        #PERSONA DEL CAMPO
        self.__inv=None
    
    def setImec(self,imec:str):
        self.__imec=imec
    
    def getImec(self):
        return self.__imec
    
    def setInv(self,inv:str):
        self.__inv=inv
    
    def getInv(self):
        return self.__inv
    
    def robot(self):
        return "An engineer is a machine for turning coffe into solutions"


def main():

    Engineer1=Ing_Multimedia()
    Engineer1.setName("Eduardo")
    Engineer1.setSemester(8)
    Engineer1.setUniversity("Universidad Militar Nueva Granada") 
    Engineer1.setImu('calculo')
    Engineer1.setApp('photoshop')
    
    Engineer2=Ing_Quimica()
    Engineer2.setName("Charlie")
    Engineer2.setSemester(8)
    Engineer2.setUniversity("Universidad de La Sabana")
    Engineer2.setQui('cerveza')
    Engineer2.setCompound('nitrogeno')
    
    Engineer3=Ing_Mecatronica()
    Engineer3.setName("Mary")
    Engineer3.setSemester(2)
    Engineer3.setUniversity("Universidad de San Buenaventura")
    Engineer3.setImec('python')
    Engineer3.setInv('aziel')
    
    
    #Aplicantes
    print(f'aplicante:{Engineer1.getName()} Language: {Engineer1.getSemester()} University: {Engineer1.getUniversity()} Favorite Subject:{Engineer1.getImu()} Favorite App: {Engineer1.getApp()} {Engineer1.xd()}')
    
    print(f'aplicante:{Engineer2.getName()} Language: {Engineer2.getSemester()} University: {Engineer2.getUniversity()} Favorite Mix:{Engineer2.getQui()} Favorite Compound: {Engineer2.phrase()}') 
    
    print(f'aplicante:{Engineer3.getName()} Language: {Engineer3.getSemester()} University: {Engineer3.getUniversity()} Favorite App: {Engineer3.getImec()} Country Person: {Engineer3.getInv()} Overload: {Engineer3.robot()}') 
    
    
if __name__=="__main__":
    main()