from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from gestor import GestorGastos
from gasto import Gasto
from ingreso import Ingreso
from fastapi import HTTPException

# Inicializamos la app
app = FastAPI(
    title="Gestor de Gastos Personales",
    version="1.0",
    description="API para registrar, consultar y calcular el saldo de tus movimientos financieros personales."
)

# Objeto para guardar los movimientos de la
gestor = GestorGastos()

# Comprobamos que la API está funcionando
@app.get("/")
def inicio():
    return {"mensaje": "API de gestor de gastos OK"}

# Heredo la clase BaseModel de la librería Pydantic para la validación de datos
class MovimientoIn(BaseModel):
    concepto: str
    cantidad: float
    fecha: date

# Endpoint de movimientos dependiendo del signo. Ingreso si es positivo
# y Gasto si es negativo
@app.post("/movimientos")
def crear_movimiento(mov: MovimientoIn):
    if mov.cantidad >= 0:
        nuevo = Ingreso(mov.concepto, mov.cantidad, mov.fecha)
    else:
        nuevo = Gasto(mov.concepto, abs(mov.cantidad), mov.fecha)

    gestor.agregar(nuevo)

    return {"mensaje": "Movimiento guardado correctamente"}

# Endpoint para listar los movimientos
@app.get("/movimientos")
def listar_movimientos():
    return [
        {
            "id": i.id,
            "concepto": i.concepto,
            "cantidad": i.importe(),
            "fecha": i.fecha
        }
        for i in gestor.movimientos
    ]

# Endpoint para obtener el saldo total
@app.get("/saldo")
def obtener_saldo():
    return {"saldo_total": gestor.saldo_total()}

# Endpoint para hacer el borrado de los movimientos por id
@app.delete("/movimientos/{id}")
def eliminar_movimiento(id: int):
    if gestor.eliminar(id):
        return {"mensaje": f"Movimiento {id} eliminado"}
    else:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")