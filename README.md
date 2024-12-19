Aqui esta la entrega final del pro# Sistema de Inventario en Python

Este proyecto es un sistema de inventario desarrollado en Python que permite gestionar productos mediante una base de datos SQLite. Ofrece funcionalidades para registrar, buscar, actualizar, eliminar y generar reportes de productos, proporcionando una solución sencilla y eficiente para el manejo de inventarios.

---

## Características Principales

- **Registrar productos:** Agrega nuevos productos a la base de datos con información como nombre, descripción, cantidad, precio y categoría.
- **Mostrar inventario:** Visualiza todos los productos registrados.
- **Actualizar productos:** Modifica la información de productos existentes.
- **Eliminar productos:** Elimina productos de la base de datos.
- **Buscar productos:** Encuentra productos por su ID.
- **Generar reportes de bajo stock:** Lista productos cuya cantidad esté por debajo de un límite especificado.

---

## Requisitos del Sistema

- Python 3.6 o superior.
- Librería SQLite3 (incluida en la instalación estándar de Python).
- Un sistema operativo compatible (Windows, macOS o Linux).

---

## Estructura del Proyecto

```
├── data/
│   └── inventario.db         # Base de datos SQLite (se crea automáticamente)
├── proyectofinal.py          # Archivo principal del sistema de inventario
├── README.md                 # Documentación del proyecto
```

---

## Instalación y Configuración

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/sistema-inventario.git
   cd sistema-inventario
   ```

2. **Crea el entorno virtual (opcional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate    # Windows
   ```

3. **Ejecuta el programa:**

   ```bash
   python proyectofinal.py
   ```

4. **El sistema creará automáticamente la base de datos en el directorio `data/` si no existe.**

---

## Uso

1. Ejecuta el programa y sigue las instrucciones del menú principal:

   ```
   Menú principal

       1) Registrar producto
       2) Mostrar el inventario
       3) Actualizar producto
       4) Eliminar producto
       5) Buscar producto
       6) Generar reporte de bajo stock

       0) Salir
   ```

2. Selecciona una opción ingresando el número correspondiente.
3. Sigue las instrucciones para completar la acción deseada.

---

## Funciones Clave

### 1. `alta_registro`
Registra nuevos productos en la base de datos.

### 2. `mostrar_registros`
Muestra todos los productos en formato tabular.

### 3. `actualizar_registro`
Actualiza los datos de un producto existente basado en su ID.

### 4. `eliminar_producto`
Elimina un producto especificado por su ID.

### 5. `buscar_registro`
Busca y muestra un producto por su ID.

### 6. `reporte_bajo_stock`
Genera un reporte de productos con cantidades por debajo de un límite especificado.

---

## Personalización

- Puedes modificar el archivo `proyectofinal.py` para ajustar las columnas de la tabla `productos` según tus necesidades:

   ```python
   campos_def = {
       'id': 'INTEGER',
       'nombre': 'TEXT NOT NULL',
       'descripcion': 'TEXT',
       'cantidad': 'INTEGER NOT NULL',
       'precio': 'REAL NOT NULL',
       'categoria': 'TEXT',
   }
   ```

- Añade, elimina o cambia los tipos de datos según tus requerimientos.

---

## Contribución

1. Haz un fork del repositorio.
2. Crea una rama para tu función o corrección:

   ```bash
   git checkout -b mi-nueva-funcion
   ```

3. Realiza tus cambios y confirma los commits:

   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```

4. Envía tus cambios al repositorio remoto:

   ```bash
   git push origin mi-nueva-funcion
   ```

5. Abre un pull request en GitHub.

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contacto

- Autor: [Ignacio Castillo] (https://github.com/CazDNB)

