class Botella():
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados


    def imprimir_datos(self):
        print("\n=== DATOS DE LA BOTELLA ===")
        print(f"Material: {self.material}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Forma: {self.forma}")
        print(f"Diseño: {self.diseño}")
        print(f"Tapa: {self.tapa}")
        print(f"Grabados: {self.grabados}")