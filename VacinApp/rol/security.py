from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Hashea la contraseña antes de almacenarla"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """Verifica que una contraseña ingresada coincida con la almacenada"""
    return pwd_context.verify(plain_password, hashed_password)