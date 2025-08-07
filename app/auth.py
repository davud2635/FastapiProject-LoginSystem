# Importerer nødvendige ting fra FastAPI
from fastapi import HTTPException, status, Depends

# Importerer JWT fra jose-biblioteket
from jose import jwt

# Tidsværktøjer til at lave token-udløbstid
from datetime import datetime, timedelta

# Bruger OAuth2-password flow til login
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# En simpel hemmelig nøgle til at signere JWT (burde gemmes i .env)
SECRET_KEY = "supersecret"

# Algoritme vi bruger til at kryptere/signere JWT
ALGORITHM = "HS256"

# Definerer hvordan vi skal hente token fra requests (typisk via "Authorization: Bearer <token>")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# En fake bruger-database (ingen rigtig database endnu)
fake_users = {
    "user": {
        "username": "davud2635",
        "password": "menzil123"  # I praksis bør man aldrig gemme passwords i klartekst
    }
}

# Funktion til at tjekke om brugeren findes og password matcher
def authenticate_user(username_input: str, password_input: str):
    user = fake_users.get(username_input)
    if not user:
        return False

    password = user["password"]
    if password != password_input:
        return False
    return user



# Funktion der laver en JWT token med udløbstid
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)  # Token udløber om 1 time
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Funktion der henter nuværende bruger fra token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        # Dekoder token og tjekker om det er gyldigt
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")  # Henter brugernavnet fra token payload.   "sub" = subject = brugernavn
        return username
    except:
        # Hvis token er forkert eller udløbet
        raise HTTPException(status_code=401, detail="Invalid token")
