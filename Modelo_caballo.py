from Modelo_animales import animales

class caballo(animales):

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El {self.nombre} se mueve de manera cuadrupeda.")

    def comunicacion(self):
        print(f"El {self.nombre} se comunica atraves de señales visuales, vocales y tactiles.") 

    def reproduccion(self):
            print(f"El {self.nombre} se reproducen cuando la yegua entra en celo.") 

    def alimentarse(self):
        print(f"El {self.nombre} se alimenta de pasto y heno.")

    def adaptacion(self):
        print(f"El {self.nombre} se adapta a su entorno mediante cambios en su comportamiento y fisiología.")

    def instintos(self):
        print(f"El {self.nombre} tiene instintos de manada y migración.")

    def descanso(self):
        print(f"El {self.nombre} descansa de pie o acostado en áreas seguras.")

    def sueño(self):
        print(f"El {self.nombre} duerme entre 2 a 4 horas al día, generalmente en períodos cortos.")

    def interaccion_social(self):
        print(f"El {self.nombre} interactúa socialmente con otros miembros de su especie a través de vocalizaciones y lenguaje corporal.")
    