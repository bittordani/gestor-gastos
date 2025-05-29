from gasto import Gasto
from ingreso import Ingreso
from datetime import date

# Crear un gasto
gasto = Gasto(concepto="Supermercado", fecha=date.today(), cantidad=50.0)

# Crear un ingreso
ingreso = Ingreso(concepto="Sueldo", fecha=date.today(), cantidad=1000.0)

# Mostrar resultados
print("Gasto:", gasto.importe())      # Debe ser -50.0
print("Ingreso:", ingreso.importe())  # Debe ser 1000.0
