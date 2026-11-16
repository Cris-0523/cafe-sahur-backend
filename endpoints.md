# Documentación de la API - Café Sahur

## 1. Información general

**Proyecto: Café Sahur Backend

Framework: Django REST Framework

URL base: `http://127.0.0.1:8000/api/`

La API permite gestionar categorías, productos, clientes, pedidos y detalles de pedidos mediante solicitudes HTTP.

## 2. Categorías

### Listar categorías

- Método: GET
- Ruta: `/api/categorias/`

### Crear categoría

- Método: POST
- Ruta: `/api/categorias/`

Ejemplo:

```json
{
    "nombre": "Bebidas",
    "descripcion": "Bebidas frías y calientes"
}
```

### Consultar, actualizar o eliminar una categoría

- Ruta: `/api/categorias/{id}/`
- Métodos: GET, PUT, PATCH, DELETE.

## 3. Productos

### Listar productos

- Método: GET
- Ruta: `/api/productos/`

### Crear producto

- Método: POST
- Ruta: `/api/productos/`

Ejemplo:

```json
{
    "nombre": "Coca Cola Espuma",
    "descripcion": "Bebida de prueba",
    "precio": 25990,
    "stock": 10,
    "imagen": "",
    "activo": true,
    "categoria": 1
}
```

### Consultar, actualizar o eliminar un producto

- Ruta: `/api/productos/{id}/`
- Métodos: GET, PUT, PATCH, DELETE.

## 4. Clientes

### Listar clientes

- Método: GET
- Ruta: `/api/clientes/`

### Crear cliente

- Método: POST
- Ruta: `/api/clientes/`

Ejemplo:

```json
{
    "nombre": "Cliente Prueba",
    "email": "prueba@cafesahur.cl",
    "telefono": "+56987654321"
}
```

El correo electrónico debe ser único y el teléfono debe cumplir el formato validado por el campo telefónico.

### Consultar, actualizar o eliminar un cliente

- Ruta: `/api/clientes/{id}/`
- Métodos: GET, PUT, PATCH, DELETE.

## 5. Pedidos

### Listar pedidos

- Método: GET
- Ruta: `/api/pedidos/`

### Crear pedido

- Método: POST
- Ruta: `/api/pedidos/`

Ejemplo:

```json
{
    "estado": "pendiente",
    "cliente": 1
}
```

La fecha se genera automáticamente y el estado inicial es pendiente si no se especifica otro valor.

### Consultar, actualizar o eliminar un pedido

- Ruta: `/api/pedidos/{id}/`
- Métodos: GET, PUT, PATCH, DELETE.

## 6. Detalles de pedidos

### Listar detalles

- Método: GET
- Ruta: `/api/detalle-pedidos/`

### Crear detalle

- Método: POST
- Ruta: `/api/detalle-pedidos/`

Ejemplo:

```json
{
    "pedido": 1,
    "producto": 1,
    "cantidad": 2,
    "precio_unitario": 25990
}
```

El sistema verifica el stock disponible antes de crear el detalle. Si existe disponibilidad, descuenta automáticamente las unidades solicitadas.

### Consultar detalle

- Método: GET
- Ruta: `/api/detalle-pedidos/{id}/`

### Actualizar detalle

- Métodos: PUT y PATCH
- Ruta: `/api/detalle-pedidos/{id}/`

Ejemplo de actualización de cantidad:

```json
{
    "cantidad": 3
}
```

El sistema ajusta el stock de acuerdo con la diferencia entre la cantidad anterior y la nueva.

Si se cambia el producto, se devuelve el stock al producto anterior y se descuentan las unidades del nuevo producto, siempre que exista disponibilidad.

### Eliminar detalle

- Método: DELETE
- Ruta: `/api/detalle-pedidos/{id}/`

Al eliminar un detalle, las unidades correspondientes se devuelven automáticamente al inventario.

## 7. Validaciones y respuestas

La API contempla las siguientes validaciones:

- No permite cantidades menores que 1.
- No permite precios menores que 1.
- No permite crear detalles cuando el stock es insuficiente.
- Valida los formatos de correo electrónico y teléfono.
- Evita correos electrónicos duplicados.
- Protege las operaciones de inventario mediante transacciones atómicas.

### Códigos HTTP principales

| Código | Significado |
|---|---|
| 200 | Solicitud realizada correctamente |
| 201 | Recurso creado correctamente |
| 400 | Error de validación o solicitud incorrecta |
| 404 | Recurso no encontrado |
| 500 | Error interno del servidor |

### Ejemplo de error por stock insuficiente

Solicitud:

```json
{
    "cantidad": 11
}
```

Respuesta:

```json
{
    "cantidad": "Stock insuficiente. Disponible: 8"
}
```

Código HTTP: `400 Bad Request`.

## 8. Herramienta de pruebas

Se utilizó la interfaz navegable de Django REST Framework para realizar solicitudes HTTP y comprobar las respuestas JSON de los endpoints.

Las pruebas permiten verificar las operaciones CRUD y las validaciones de inventario.