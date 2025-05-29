from datetime import date

class Movimiento:
    def __init__(self, concepto: str, fecha: date):
        self.concepto = concepto
        self.fecha = fecha

    def importe(self) -> float:
        return 0.0
