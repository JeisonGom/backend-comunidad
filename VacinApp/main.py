from fastapi import FastAPI, Request, Depends
from login.auth import router as auth_router
from login.middleware import authenticate_token
from comunidad.community import router as community_router 
import sys
import os
from roles.routes.users import router as users_router
from roles.routes.communities import router as communities_router


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = FastAPI()

# Registrar rutas de autenticación
app.include_router(auth_router)
app.include_router(community_router)
app.include_router(users_router, prefix="/users", tags=["Usuarios"])
app.include_router(communities_router, prefix="/communities", tags=["Comunidades"])



@app.get("/perfil")
def perfil(request: Request, user: str = Depends(authenticate_token)):
    """obtiene el perfil del usuario autenticado"""
    return {"message": "Acceso autorizado", "user": request.state.user}

@app.get("/datos")
def datos_sensibles(request: Request, user: str = Depends(authenticate_token)):
    """obtiene datos sensibles del usuario autenticado"""
    return {"message": "Datos protegidos", "user": request.state.user}