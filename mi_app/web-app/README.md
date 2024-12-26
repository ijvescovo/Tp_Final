# Proyecto de Gestión de Productos

Este proyecto es una aplicación web para la gestión de productos utilizando Python y SQLite. Permite registrar, buscar, actualizar, eliminar y listar productos en una base de datos.

## Estructura del Proyecto

```
web-app
├── src
│   ├── app.py                # Punto de entrada de la aplicación.
│   ├── templates             # Plantillas HTML.
│   │   ├── base.html         # Plantilla base con estructura común.
│   │   ├── index.html        # Página de inicio.
│   │   ├── register.html     # Formulario para registrar nuevos productos.
│   │   ├── search.html       # Página para buscar productos.
│   │   ├── update.html       # Formulario para actualizar productos.
│   │   ├── delete.html       # Página para eliminar productos.
│   │   └── list.html         # Listado completo de productos.
│   ├── static
│   │   └── css               # Archivos CSS.
│   │       └── styles.css    # Estilos avanzados para las páginas.
│   └── db                    # Base de datos.
│       └── inventario.db     # Base de datos SQLite.
├── requirements.txt          # Dependencias necesarias para ejecutar la aplicación.
└── README.md                 # Documentación del proyecto.
```

## Requisitos

- Python 3.x
- Flask
- SQLite

## Instalación

1. Clona el repositorio o descarga los archivos del proyecto.
2. Navega al directorio del proyecto.
3. Instala las dependencias necesarias ejecutando:

```
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/app.py
```

Luego, abre tu navegador y visita `http://127.0.0.1:5000` para acceder a la aplicación.

## Funcionalidades

- **Registro de Productos**: Permite agregar nuevos productos a la base de datos.
- **Búsqueda de Productos**: Consulta los detalles de un producto específico.
- **Actualización de Productos**: Modifica la cantidad de un producto existente.
- **Eliminación de Productos**: Elimina productos de la base de datos.
- **Listado de Productos**: Muestra todos los productos almacenados.
- **Reporte de Bajo Stock**: Lista productos con cantidad bajo mínimo.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.