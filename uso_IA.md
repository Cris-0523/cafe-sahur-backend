# Declaración de uso de Inteligencia Artificial

## Proyecto: Café Sahur Backend

### 1. Herramientas utilizadas

Durante el desarrollo del proyecto se utilizó ChatGPT (OpenAI) como herramienta de apoyo para el aprendizaje, programación y resolución de problemas.

### 2. Participación estimada de IA por archivo

Los siguientes porcentajes corresponden a estimaciones sobre la participación de la IA en cada archivo.

| Archivo | Uso estimado de IA | Descripción |
|---|---:|---|
| `models.py` | 35% | Orientación sobre estructura de modelos y relaciones entre entidades. |
| `views.py` | 60% | Apoyo en la implementación y modificación de endpoints y lógica de inventario. |
| `serializers.py` | 30% | Apoyo en la revisión de serializadores y validaciones. |
| `urls.py` | 10% | Consulta sobre configuración de rutas y utilización de DefaultRouter. |
| `config/urls.py` | 10% | Orientación sobre configuración de rutas principales. |


### 3. Respuestas sobre el uso de inteligencia artificial

**1. ¿En qué aspectos del proyecto utilizaron inteligencia artificial?**

Utilizamos ChatGPT principalmente para resolver dudas de Django REST Framework, revisar errores, mejorar la lógica de los endpoints y desarrollar el control automático de inventario. También fue utilizado como apoyo para comprender las relaciones entre los modelos y documentar la API.

**2. ¿Qué partes del código fueron desarrolladas principalmente por ustedes?**

En la definición de los modelos, relaciones entre entidades, configuración de la API y ejecución de las operaciones CRUD. También se realizaron modificaciones y pruebas para adaptar las funcionalidades a los requisitos del proyecto.

**3. ¿Qué errores o problemas encontraron en las respuestas generadas por IA?**

Algunas sugerencias necesitaron ajustes para adaptarse a la estructura real del proyecto y a los nombres de los campos y relaciones. También fue necesario corregir detalles durante las pruebas y comprobar que las modificaciones no afectaran el funcionamiento del inventario.

**4. ¿Cómo verificaron que el código sugerido funcionaba correctamente?**

Verificamos el funcionamiento mediante la interfaz navegable. Realizamos solicitudes GET, POST, PUT, PATCH y DELETE, comprobando las respuestas HTTP y los datos JSON. También probamos el descuento y la devolución de stock, además de los errores por cantidades superiores al inventario disponible.

**5. ¿Qué conocimientos adquirieron durante el desarrollo?**

Aprendimos a trabajar con Django REST Framework, crear modelos y relaciones entre entidades, utilizar serializadores y ViewSets, implementar operaciones CRUD y manejar solicitudes HTTP. Además, comprendimos cómo controlar el inventario mediante transacciones y validaciones para mantener la consistencia de los datos.

### 4. Declaración final

La inteligencia artificial fue utilizada como herramienta de apoyo durante el desarrollo del proyecto. El equipo revisó, adaptó y probó las sugerencias antes de incorporarlas, manteniendo la responsabilidad sobre el funcionamiento y resultado final del backend.