class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self,color):
        Lista = ["rojo","verde","amarillo","negro","blanco"]
        if color in Lista:
            self.color = color
class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados = cantidadCreados
    def cantidadAsientos(self):
        numero = 0
        for i in range(0,len(self.asientos)):
            if isinstance(self.asientos[i],Asiento) == True:
                numero = numero + 1
        return numero
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in range(0,len(self.asientos)):
                if isinstance(self.asientos[i],Asiento) == True:
                    if self.registro != self.asientos[i].registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    def cambiarRegistro(self,registro):
        self.registro = registro
    def asignarTipo(self,tipo):
        ListaTipo = ["electrico","gasolina"]
        if tipo in ListaTipo:
            self.tipo = tipo


        


