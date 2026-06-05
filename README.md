# LOYALTEE API

Backend LOYALTEE en Django REST Framework para gestión de fidelización de clientes de una tienda de ropa deportiva.

## Descripción del Proyecto

LOYALTEE es un sistema integral de fidelización diseñado para tiendas deportivas que buscan potenciar la relación con sus clientes mediante un programa de puntos, recompensas y niveles de membresía. El backend proporciona una API REST robusta que permite gestionar usuarios, compras, puntos de fidelización, recompensas y devoluciones.

El sistema fue desarrollado con Django REST Framework siguiendo mejores prácticas de arquitectura de API REST, incluyendo autenticación JWT, paginación, filtrado avanzado y validaciones complejas.

## Características Principales

### Gestión de Usuarios y Autenticación
- Registro de nuevos usuarios con validación de email único
- Autenticación mediante JWT (JSON Web Tokens)
- Creación automática de perfil de usuario y sistema de puntos al registrarse
- Gestión de sesiones de autenticación
- Cambio de contraseña con validación de contraseña actual
- Actualización de perfil de usuario

### Sistema de Fidelización
- Acumulación de puntos por cada compra realizada
- Cuatro niveles de membresía basados en puntos acumulados:
  - Bronze: 0 a 799 puntos
  - Plata: 800 a 1999 puntos
  - Oro: 2000 a 4999 puntos
  - Platino: 5000+ puntos
- Cálculo automático de nivel según puntos acumulados
- Registro de puntos usados en canjes de recompensas

### Gestión de Compras
- Registro de compras con múltiples métodos de pago
- Desglose de items por compra
- Historial completo de compras del usuario
- Automatización de acumulación de puntos por compra
- Métodos de pago soportados: Tarjeta, Efectivo, PayPal, Transferencia

### Catálogo de Productos
- Organización de productos por categorías
- Registro de información completa del producto: nombre, descripción, marca, talla, color
- Control de stock disponible
- Precio regular y precio con descuento
- Asignación de puntos otorgados por producto
- Productos destacados para promoción

### Sistema de Recompensas
- Catálogo de recompensas disponibles
- Validación de puntos suficientes antes de canjear
- Actualización automática de stock tras canje
- Deactivación automática de recompensas sin stock
- Registro de todas las recompensas canjeadas

### Gestión de Devoluciones
- Solicitud de devolución con motivos predefinidos
- Estados de devolución: Solicitada, Aprobada, Rechazada, En Tránsito, Recibida, Procesada
- Cálculo automático de reembolso
- Recuperación de puntos utilizados en devoluciones
- Notas administrativas para cada devolución

## Estructura de la Base de Datos

### Tablas principales

**User (Django Auth)**
- Usuario base de Django con email y contraseña
- Soporte para usuarios staff (administradores)

**UserProfile**
- Perfil extendido del usuario
- Teléfono, rol (cliente/staff)
- Relación uno-a-uno con User

**PuntosFidelizacion**
- Puntos acumulados y usados
- Nivel actual del cliente
- Último registro de actualización

**Compra**
- Registro de transacción
- Total, método de pago
- Fecha de compra
- Relación con User

**CompraItem**
- Items individuales dentro de una compra
- Nombre, descripción, cantidad, precios
- Relación muchos-a-uno con Compra

**Categoria**
- Clasificación de productos deportivos
- Descripción e ícono

**Producto**
- Catálogo de productos
- SKU único por producto
- Precios regular y descuento
- Puntos otorgados
- Relación con Categoria

**Recompensa**
- Ofertas canjeables por puntos
- Stock y estado
- Puntos necesarios para canjear

**RecompensasReclamadas**
- Registro de canjes realizados
- Estado del canje
- Puntos gastados
- Relación muchos-a-uno con User y Recompensa

**Devolucion**
- Solicitudes de devolución
- Estados y motivos predefinidos
- Monto de reembolso
- Puntos recuperados
- Relación con Compra y User

**AuthSession**
- Registro de sesiones activas
- Token y fecha de expiración
- Estado de la sesión

## Endpoints de API

### Autenticación
- `POST /api/auth/register/` - Registro de usuario
- `POST /api/auth/login/` - Login y obtención de tokens
- `POST /api/auth/logout/` - Cierre de sesión

### Usuarios
- `GET /api/users/me/` - Obtener perfil del usuario autenticado
- `PATCH /api/users/update-profile/` - Actualizar perfil
- `POST /api/users/change-password/` - Cambiar contraseña

### Compras
- `GET /api/compras/` - Listar compras del usuario
- `POST /api/compras/` - Crear nueva compra
- `GET /api/compras/{id}/` - Detalle de compra específica

### Puntos de Fidelización
- `GET /api/puntos/{id}/` - Obtener puntos del usuario
- `PUT /api/puntos/acumular/` - Acumular puntos

### Recompensas
- `GET /api/recompensas/` - Listar recompensas disponibles
- `POST /api/recompensas/canjear/` - Canjear recompensa

## Tecnologías Utilizadas

- **Framework:** Django 6.0.5
- **API:** Django REST Framework 3.17.1
- **Autenticación:** JWT (djangorestframework-simplejwt)
- **Base de datos:** PostgreSQL / SQLite
- **Servidor:** Gunicorn
- **Proxy reverso:** Nginx
- **Validación:** django-filter, python-decouple

## Requisitos del Sistema

- Python 3.12+
- pip o Poetry para gestión de dependencias
- PostgreSQL 12+ (opcional, incluye SQLite por defecto)
- Virtualenv para aislamiento de dependencias

## Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/KarlaRosales13F/Loyalty-Backend.git
cd Loyalty-Backend
```

2. Crear y activar virtualenv:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
```

5. Aplicar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario (opcional):
```bash
python manage.py createsuperuser
```

7. Ejecutar servidor de desarrollo:
```bash
python manage.py runserver
```

## Despliegue en Producción

El proyecto está configurado para despliegue en VPS con:

- Gunicorn como servidor WSGI
- Nginx como proxy reverso
- Systemd para gestión del servicio
- PostgreSQL como base de datos principal

Ubicación en VPS: `/opt/loyaltee/`

## Archivos de Configuración

- `config/settings.py` - Configuración principal de Django
- `pyproject.toml` - Dependencias del proyecto
- `requirements.txt` - Dependencias para pip
- `postman_collection_loyaltee.json` - Colección de Postman para testing
- `.env` - Variables de entorno (no incluido en repositorio)

## Contacto

Desarrollado por Karla Rosales

Repositorio: https://github.com/KarlaRosales13F/Loyalty-Backend
