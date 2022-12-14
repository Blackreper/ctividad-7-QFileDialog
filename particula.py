

class Particula:
    def __init__(self, id = 0.0, origen_X= 0.0, origen_Y= 0.0, 
                destino_X= 0.0, destino_Y= 0.0, velocidad= 0.0, 
                red= 0.0, green= 0.0, blue= 0.0):
        self.__id = repr(id)
        self.__origen_x = repr(origen_X)
        self.__origen_y = repr(origen_Y)
        self.__destino_x = repr(destino_X)
        self.__destino_y = repr(destino_Y)
        self.__velocidad = repr(velocidad)
        self.__red = repr(red)
        self.__green = repr(green)
        self.__blue = repr(blue)
        #self.__distancia = repr(distancia_euclidiana(origen_X, origen_Y, destino_X, destino_Y))
    
    def __str__(self):
        return(
            'ID: ' + self.__id + '\n' +
            'Origen X: ' + self.__origen_x + '\n' +
            'Origen Y: ' + self.__origen_y + '\n' +
            'Destino X: ' + self.__destino_x + '\n' +
            'Destino Y: ' + self.__destino_y + '\n' +
            'Velocidad: ' + self.__velocidad + ' M/S \n' +
            'Rojo: ' + self.__red + '\n' +
            'Verde: ' + self.__green + '\n' +
            'Azul: ' + self.__blue + '\n'
            #'Distancia: ' + self.__distancia +  ' M \n' 
            )
    
    def to_dict(self):
        return {
            "id": self.__id,
            "origen_X": self.__origen_x,
            "origen_Y": self.__origen_y,
            "destino_X": self.__destino_x,
            "destino_Y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
