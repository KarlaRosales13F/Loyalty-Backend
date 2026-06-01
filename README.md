# LOYALTEE API

Backend LOYALTEE en Django REST Framework para gestión de fidelización de clientes de una tienda de ropa deportiva.

## Funcionalidades

- Registro e inicio de sesión con JWT.
- Gestión de clientes y usuarios.
- Registro de compras y acumulación de puntos.
- Canje de recompensas.
- Niveles de fidelización.

## Endpoints principales

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/logout`
- `GET /api/users`
- `GET /api/users/:id`
- `POST /api/compras`
- `GET /api/compras`
- `GET /api/puntos/:id_user`
- `PUT /api/puntos/acumular`
- `GET /api/recompensas`
- `POST /api/recompensas/canjear`

## Ejecución

1. Configura las variables de entorno necesarias.
2. Ejecuta migraciones.
3. Inicia el servidor local con Django.
