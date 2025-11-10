from Modelo_animales import animales

class escarabajo(animales):

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El {self.nombre} se mueve caminando y volando.")

    def comunicacion(self):
        print(f"El {self.nombre} se comunica a través de señales químicas y táctiles.") 

    def reproduccion(self):
        print(f"El {self.nombre} se reproducen mediante la fertilización interna y ponen huevos.") 

    def alimentarse(self):
        print(f"El {self.nombre} se alimenta de materia orgánica en descomposición y vegetación.")

    def adaptacion(self):
        print(f"El {self.nombre} se adapta a su entorno mediante cambios en su comportamiento y fisiología.")

    def instintos(self):
        print(f"El {self.nombre} tiene instintos de búsqueda de alimento y reproducción.")

    def descanso(self):
        print(f"El {self.nombre} descansa en lugares oscuros y protegidos.")

    def sueño(self):
        print(f"El {self.nombre} duerme en períodos cortos a lo largo del día y la noche.")

    def interaccion_social(self):
        print(f"El {self.nombre} interactúa socialmente con otros miembros de su especie a través de señales químicas y táctiles.")
