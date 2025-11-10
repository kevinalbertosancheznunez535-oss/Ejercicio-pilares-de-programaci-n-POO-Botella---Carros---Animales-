from Modelo_animales import animales
class caiman(animales):

    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)

    def moverse(self):
        print(f"El {self.nombre} se mueve nadando y caminando.")

    def comunicacion(self):
        print(f"El {self.nombre} se comunica a través de vocalizaciones, posturas corporales y señales químicas.") 

    def reproduccion(self):
        print(f"El {self.nombre} se reproducen mediante la fertilización interna y ponen huevos.") 

    def alimentarse(self):
        print(f"El {self.nombre} se alimenta de peces, aves y mamíferos pequeños.")

    def adaptacion(self):
        print(f"El {self.nombre} se adapta a su entorno mediante cambios en su comportamiento y fisiología.")

    def instintos(self):
        print(f"El {self.nombre} tiene instintos de caza y territorialidad.")

    def descanso(self):
        print(f"El {self.nombre} descansa en la orilla del agua o en áreas sombreadas.")

    def sueño(self):
        print(f"El {self.nombre} duerme varias horas al día, generalmente durante el día.")

    def interaccion_social(self):
        print(f"El {self.nombre} interactúa socialmente con otros miembros de su especie a través de vocalizaciones y lenguaje corporal.")
