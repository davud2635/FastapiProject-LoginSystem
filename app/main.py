# Importerer FastAPI, Depends og HTTPException til at bygge API’en
from fastapi import FastAPI, Depends, HTTPException

# Importerer auth- og AI-funktioner vi har lavet
from app.auth import authenticate_user, create_token, get_current_user
from app.ai import run_ai

# Importerer formulardata-håndtering for login
from fastapi.security import OAuth2PasswordRequestForm

# Opretter FastAPI-appen
app = FastAPI()

# Endpoint til at logge ind og få en JWT token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Tjekker om brugeren findes og har korrekt password
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect login")
    # Opretter og returnerer token hvis login er korrekt
    token = create_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

# Endpoint hvor man kan bruge AI-funktionen, men kun hvis man er logget ind
@app.get("/ai")
def use_ai(prompt: str, user: str = Depends(get_current_user)):
    # Kører prompten gennem AI-funktionen
    result = run_ai(prompt)
    return {"result": result}
