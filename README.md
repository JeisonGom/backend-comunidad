📌 Descripción

Este backend fue desarrollado para VecinApp, una plataforma diseñada para conectar comunidades y facilitar la comunicación entre vecinos. Proporciona funcionalidades como:
✅ Creación y gestión de comunidades.
✅ Autenticación de usuarios.
✅ Asociación de usuarios a comunidades mediante código o nombre.

🚀 Tecnologías utilizadas
🔹 Lenguaje: Python
🔹 Framework: FastAPI
🔹 Base de datos: PostgreSQL
🔹 ORM: SQLAlchemy
🔹 Autenticación: JWT

🔧 Instalación y configuración

1️⃣ Clona el repositorio
git clone https://github.com/JeisonGom/backend-comunidad.git

2️⃣ Instala las dependencias:
pip install -r requirements.txt


3️⃣ Configura la base de datos en .env:
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/database


4️⃣ Ejecuta el servidor:
uvicorn main:app --reload


5️⃣ Accede a la API:
http://localhost:8000/docs


📌 Endpoints principales
🔹 POST /community/join → Une a un usuario a una comunidad por código o nombre.
🔹 GET /users/{id} → Obtiene datos del usuario.
🔹 POST /auth/login → Autentica a un usuario y genera un token JWT.
📜 Licencia
Este proyecto está bajo la licencia MIT
