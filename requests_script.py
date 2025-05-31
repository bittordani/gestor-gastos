import requests

URL = "http://127.0.0.1:8000"

# Creamos una serie de movimientos positivos y negativos
movimientos = [
    {"concepto": "Nómina mayo", "cantidad": 2400.0, "fecha": "2024-05-26"},
    {"concepto": "Hipoteca", "cantidad": -400.0, "fecha": "2024-05-30"},
    {"concepto": "Gasolina", "cantidad": -80.0, "fecha": "2024-05-30"},
    {"concepto": "Supermercado", "cantidad": -120.0, "fecha": "2024-05-30"},
]

# Imprimimos en pantalla los mensajes correspondiente a los movimientos
for mov in movimientos:
    response = requests.post(f"{URL}/movimientos", json=mov)
    print(f"POST {mov['concepto']}: {response.json()}")

# Obtenemos la lista de movimientos
response = requests.get(f"{URL}/movimientos")
print("\nGET /movimientos:")
for mov in response.json():
    print(mov)

# Hacemos el borrado del movimiento con id 3
id_borrado = 3
response = requests.delete(f"{URL}/movimientos/{id_borrado}")
print(f"\nDELETE /movimientos/{id_borrado}:", response.json())

# Listamos el saldo tras las operaciones anteriores
response = requests.get(f"{URL}/saldo")
print("\nGET /saldo:", response.json())
