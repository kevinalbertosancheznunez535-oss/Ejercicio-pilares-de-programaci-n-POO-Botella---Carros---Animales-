from Modelo_2vehiculo import Vehiculo
# Clase hija 2 - Van
class Van(Vehiculo):
    def tipo_seguridad(self):
        print("La van tiene cinturones en todos los asientos y frenos hidráulicos.")

    def funcionamiento(self):
        super().sistema_de_espejos()
        super().climatizacion()
        super().sistema_de_ventanas()
        super().aceleracion_y_frenado()