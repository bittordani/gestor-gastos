from movimiento import Movimiento
from datetime import date

# Clase de Gasto que hereda de Movimiento
class Gasto(Movimiento):
    def __init__(self, concepto: str, cantidad: float, fecha: date):
        super().__init__(concepto, fecha)
        self.cantidad = cantidad

    def importe(self):
        return -self.cantidad # Definimos que el gasto tiene importe negativo