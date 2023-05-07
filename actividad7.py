import csv
class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = None
    def __init__(self,num,dni,nom,ap,mill):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas_acum = mill
    def getNumViajero(self):
        return(self.__num_viajero)
    def getTotalMillas(self):
        return(self.__millas_acum)
    def getDni(self):
        return(self.__dni)
    def getNombre(self):
        return(self.__nombre)
    def getApellido(self):
        return(self.__apellido)
    def __add__(self,otrasmillas):
        return self.__millas_acum + otrasmillas.getTotalMillas()
    def __gt__(self,otralista):
        if(self.__millas_acum > otralista.getTotalMillas()):
            max = self.__millas_acum
        else:
            max = otralista.getTotalMillas()
        return max
    def __sub__(self,otro):
        return ViajeroFrecuente(self.__millas_acum,otro.getTotalMillas())
    def __eq__(self,otro):
        return (self.__millas_acum==otro.getTotalMillas())
class manejadorViajero:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def agregarViajero(self,unviajero):
        self.__lista.append(unviajero)
    def testViajero(self):
        archivo = open('datosviajero.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            num = fila[0]
            dni = fila[1]
            nom = fila[2]
            ape = fila[3]
            mill = int(fila[4])
            unViajero = ViajeroFrecuente(num,dni,nom,ape,mill)
            self.agregarViajero(unViajero)
            archivo.close()
    def buscaViajero(self,num):
        i=0
        Retorno = None
        b = False
        while not b and i < len(self.__listaViajero):
            if self.__listaViajero[i].getNumViajero()==num:
            b =True
            Retorno=i
        else:
            i+=1
        return Retorno
    def getMillas(self,n):
        return(self.__listaViajero[n].getTotalMillas())
    def acumularMillas(self,nuevas_millas,n):
        m = self.__listaViajero[n].acumularMillas1(nuevas_millas)
        return m
    def canjearMillas(self,cant,n):
        self.__listaViajero[n].canjearMillas1(cant)
        return
    def comparaViajeros(self,num,n):
        b = self.__listaViajero[n]==num
        if(b==True):
            print('Son Iguales')
        else:
            print('No son Iguales')
    def comparaMillas(self):
        i=0
        maximo = max(self.__listaViajero)
        for i in range(len(self.__listaViajero)):
            if self.__listaViajero[i].getTotalMillas() == maximo.getTotalMillas():
                print("El viajero",self.__listaViajero[i].getNumViajero(),"tiene el maximo de millas.")
        