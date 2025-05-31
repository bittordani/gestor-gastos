# 📊 Gestor de Gastos - API con FastAPI
Desarrollo de una API para llevar el control de los movimientos mensuales de tus finanzas personales.
Permite registrar ingresos y gastos, consultar los movimientos almacenados y eliminar aquellos que contengan errores en su inserción.


## Tecnologías

- Python
- FastAPI
- Pydantic
- Request


## Funcionalidad

- Inserción de movimientos de capital, tanto ingresos como gastos
- Consulta de todos los movimientos registrados
- Eliminación de registros
- Consulta del saldo actual


## Manual de usuario

1. Clona el repositorio

git clone git@github.com:bittordani/gestor-gastos.git
cd gestor-gastos

2. Ejecuta la API:

uvicorn main:app --reload

3. Accede a la documentación automática:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

4. Ejecuta el script de prueba:

python requests_script.py


## Autor
Proyecto desarrollado por Víctor Daniel Martínez, como parte del módulo de programación avanzada con FastAPI
para el máster de Inteligencia Artificial, Cloud Computing y Devops de PontIa

