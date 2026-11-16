# cafe-sahur-backend
# Café Sahur - Backend

API REST desarrollada con Django y Django REST Framework para la gestión de una cafetería.

## 1. Descripción del proyecto

Café Sahur es un sistema backend que permite administrar productos, categorías, clientes y pedidos de una cafetería. También permite gestionar los detalles de cada pedido y controlar automáticamente el inventario.

El proyecto fue desarrollado de manera independiente del frontend utilizado en la Evaluación 1.

## 2. Tecnologías utilizadas

- Python
- Django 4.2.30
- Django REST Framework 3.16.1
- SQLite
- django-phonenumber-field
- phonenumbers

## 3. Modelos del sistema

El proyecto contiene cinco modelos principales:

- **Categoría:** almacena el nombre y descripción de las categorías.
- **Producto:** registra nombre, descripción, precio, stock, imagen, estado y categoría.
- **Cliente:** almacena nombre, correo electrónico y teléfono.
- **Pedido:** registra fecha, estado y cliente asociado.
- **DetallePedido:** relaciona pedidos con productos, registra cantidades, precios unitarios y calcula automáticamente el subtotal.

### Relaciones principales

- Una categoría puede tener varios productos.
- Un cliente puede tener varios pedidos.
- Un pedido puede contener varios detalles.
- Cada detalle está asociado a un producto.

## 4. Funcionalidades

- CRUD de categorías.
- CRUD de productos.
- CRUD de clientes.
- CRUD de pedidos.
- CRUD de detalles de pedidos.
- Descuento automático de stock al agregar productos a un pedido.
- Actualización del inventario al modificar cantidades.
- Devolución del stock al eliminar detalles de pedidos.
- Validación para impedir ventas con stock insuficiente.
- Validación de cantidades y precios positivos.
- Cálculo automático del subtotal de cada detalle.

## 5. Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Cris-0523/cafe-sahur-backend.git
cd cafe-sahur-backend
```

Crear un entorno virtual:

```bash
python3 -m venv .venv
```

Activar el entorno virtual en macOS/Linux:

```bash
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## 6. Migraciones

Ejecutar las migraciones para preparar la base de datos:

```bash
python manage.py migrate
```

Si se realizan modificaciones a los modelos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 7. Ejecución del servidor

Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

El backend estará disponible en:

http://127.0.0.1:8000/

La API se encuentra disponible bajo:

http://127.0.0.1:8000/api/

## 8. Endpoints principales

| Método | Ruta | Descripción |
|---|---|---|
| GET, POST | /api/categorias/ | Listar y crear categorías |
| GET, PUT, PATCH, DELETE | /api/categorias/{id}/ | Gestionar una categoría |
| GET, POST | /api/productos/ | Listar y crear productos |
| GET, PUT, PATCH, DELETE | /api/productos/{id}/ | Gestionar un producto |
| GET, POST | /api/clientes/ | Listar y crear clientes |
| GET, PUT, PATCH, DELETE | /api/clientes/{id}/ | Gestionar un cliente |
| GET, POST | /api/pedidos/ | Listar y crear pedidos |
| GET, PUT, PATCH, DELETE | /api/pedidos/{id}/ | Gestionar un pedido |
| GET, POST | /api/detalle-pedidos/ | Listar y crear detalles |
| GET, PUT, PATCH, DELETE | /api/detalle-pedidos/{id}/ | Gestionar un detalle |

La documentación detallada de solicitudes y ejemplos se encuentra en `ENDPOINTS.md`.

## 9. Control de inventario

La gestión de inventario se implementa especialmente en las operaciones de detalles de pedidos.

Al crear un detalle, el sistema verifica que exista stock suficiente y descuenta las unidades correspondientes.

Al modificar la cantidad, se ajusta el inventario según la diferencia.

Al eliminar un detalle, las unidades correspondientes se devuelven al inventario.

Estas operaciones utilizan transacciones atómicas para proteger la consistencia de los datos.

## 10. Pruebas

Las operaciones de la API fueron verificadas mediante la interfaz navegable de Django REST Framework.

Se realizaron pruebas de creación, consulta, actualización y eliminación, además de validaciones relacionadas con el inventario.

Las evidencias se encuentran organizadas en la carpeta `evidencias/`.

## 11. Repositorio

GitHub:

https://github.com/Cris-0523/cafe-sahur-backend

## 12. Archivos adicionales

- `requirements.txt`: dependencias necesarias.
- `ENDPOINTS.md`: documentación de los endpoints.
- `USO_IA.md`: declaración del uso de herramientas de inteligencia artificial.