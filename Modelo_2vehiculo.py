class Vehiculo:
    def __init__(self):
        self.modelo = ""
        self.color = ""
        self.motor = ""
        self.numero_puertas = 0
        self.capacidad_pasajeros = 0
        self.tipo_combustible = ""

    def ingresar_datos(self):
        self.modelo = input("Ingrese el modelo: ")
        self.color = input("Ingrese el color: ")
        self.motor = input("Ingrese el tipo de motor: ")
        self.numero_puertas = int(input("Ingrese el número de puertas: "))
        self.capacidad_pasajeros = int(input("Ingrese la capacidad de pasajeros: "))
        self.tipo_combustible = input("Ingrese el tipo de combustible: ")
        
    def imprimir_datos(self):
        print("\n=== DATOS DEL VEHÍCULO ===")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Número de puertas: {self.numero_puertas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Tipo de combustible: {self.tipo_combustible}")
    
    def arranque(self):
        print(f"El {self.modelo}  está arrancando.")
    def apagado(self):
        print(f"El {self.modelo} se está apagando.")
    def aceleracion_y_frenado(self):
        print(f"El {self.modelo} está acelerando y frenando.")
    def sistema_direccion(self):
        print("El sistema de dirección está funcionando correctamente.")
    def climatizacion(self):
        print("El sistema de climatización está activado.")
    def luces(self):
        print(f"Las luces del {self.modelo} están encendidas.")
    def sistema_de_ventanas(self):
        print("Las ventanas están funcionales.")
    def sistema_de_espejos(self):
        print("Los espejos están ajustados correctamente.")