# TeamBoard App - Checkpoint 01

Este proyecto es una aplicación web funcional que muestra los integrantes de un equipo de trabajo, las funcionalidades que cada uno implementó y el estado de sus respectivos servicios. La solución está íntegramente contenedorizada utilizando Docker y Docker Compose.

## Arquitectura
La aplicación se compone de cuatro servicios principales que trabajan de forma coordinada:
- **Frontend**: Interfaz de usuario que consume datos de la API.
- **Backend**: API REST en Python (Flask) que gestiona la lógica de negocio.
- **Database**: Motor de base de datos PostgreSQL para el almacenamiento persistente.
- **Portainer**: Herramienta de gestión y monitoreo de los contenedores.

## Integrantes del Grupo
| Nombre y Apellido | Legajo | Feature | Servicio |
| :--- | :--- | :--- | :--- |
| **Franco Oyhenart** | 33555 | Feature 01 & 03 | Infraestructura / Backend |
| **Esteban Trillo** | 33728 | Feature 02 | Frontend |
| **Brenda Conti** | 33717 | Feature 04 | Database |
| **Lautaro Flores** | 33411 | Feature 05 | Monitoreo |

## Requisitos
Para ejecutar este proyecto es necesario contar con:
- Docker Desktop o Docker Engine.
- Docker Compose.

## Instalación y Ejecución
1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/IstFranco/is-2026-checkpoint-01.git](https://github.com/IstFranco/is-2026-checkpoint-01.git)
   cd is-2026-checkpoint-01

2. **Levantar los servicios**:
   Asegurarse de configurar las variables de entorno en un archivo `.env` y luego ejecutar:
   ```bash
   docker compose up -d --build