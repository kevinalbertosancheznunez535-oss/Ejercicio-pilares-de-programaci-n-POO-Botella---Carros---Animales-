from Modelo_Botella import Botella
# Clase hija 1 - Botella Plástica
class BotellaPlastica(Botella):
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        super().__init__(material, capacidad, forma, diseño, tapa, grabados)

    def contener_liquidos(self):
        print("La botella plástica puede contener líquidos sin riesgo de romperse.")

    def cierre_hermetico(self):
        print("Posee un cierre con tapa roscada.")

    def facilitar_el_vertido(self):
        print("El vertido en esta botella es más fácil.")

    def transporte(self):
        print("El transporte de esta botella es liviano y sin riesgo.")

    def manejo(self):
        print("El manejo es práctico y cómodo.")

    def compatibilidad_con_bebidas_calientes_frias(self):
        print("Apta para bebidas frías. Con bebidas calientes puede deformarse.")

    def reutilizacion(self):
        print("Reuilizable:")

    def transparencia(self):
        print("El líquido es visible a través del plástico transparente.")