from Modelo_2vehiculo import Vehiculo
# Clase hija 3 - Volqueta
class Volqueta(Vehiculo):
    def tipo_seguridad(self):
        print("La volqueta tiene frenos de aire y sistema de estabilidad reforzado.")

    def funcionamiento(self):
        super().arranque()
        super().aceleracion_y_frenado()
        super().sistema_direccion()
        super().luces()
        super().sistema_de_ventanas()
        super().sistema_de_espejos()