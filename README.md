
# 🚀 FastAPI Project – Login System

Velkommen! Dette er et FastAPI-baseret projekt med integration til OpenAI API. Projektet er sat op til samarbejde med GitHub og CI/CD workflows.

---

## 📦 Krav

- **Python 3.11.9**  
  [Download Python 3.11.9](https://www.python.org/downloads/release/python-3119/)

- **Git**  
  [Download Git](https://git-scm.com/downloads)

- (Valgfrit) **PyCharm** eller anden Python-kompatibel IDE

---

## ⚙️ Installation på Windows

### 1. Klon projektet

Åbn GitHub Desktop eller terminalen:

```bash
git clone https://github.com/<DIT-BRUGERNAVN>/FastApiProject-LoginSystem.git
cd FastApiProject-LoginSystem
````

### 2. Opret og aktivér et virtuelt miljø

```bash
python -m venv .venv
.venv\Scripts\activate
```

> Du burde nu se `(.venv)` foran din terminalprompt – det betyder miljøet er aktivt.

### 3. Installer afhængigheder

```bash
pip install -r requirements.txt
```

> Mangler `requirements.txt`? Kontakt repo-ejeren eller kør `pip freeze > requirements.txt` hvis du har de rette pakker installeret.

---

## 🔐 Miljøvariabler

Vi bruger en `.env`-fil til at gemme følsomme oplysninger som API-nøgler.

### 1. Kopiér eksempel-filen

```bash
copy .env.example .env
```

### 2. Indsæt din OpenAI API-nøgle

Åbn `.env` og tilføj:

```env
OPENAI_API_KEY=din_openai_api_nøgle_her
```

---

## 🚀 Kør projektet

Kør FastAPI-serveren lokalt:

```bash
uvicorn app.main:app --reload
```

> Er din entrypoint anderledes, fx `app.ai:app`, så ret kommandoen derefter.

Gå derefter til:
`http://127.0.0.1:8000`

For at se dokumentation (Swagger UI):
`http://127.0.0.1:8000/docs`

---

## 👨‍💻 Sådan bidrager du

1. Opret en ny feature-branch:

   ```bash
   git checkout -b feature/mit-feature-navn
   ```

2. Lav dine ændringer

3. Commit og push:

   ```bash
   git add .
   git commit -m "Tilføjer nyt feature"
   git push origin feature/mit-feature-navn
   ```

4. Lav en **Pull Request** via GitHub

---

## ✅ CI/CD og automatiske checks

Når du opretter en pull request, kører automatiske test/checks via **GitHub Actions** *(hvis konfigureret)* for at sikre kvalitet og stabilitet.

---

## 🧼 `.gitignore` forklaring

Disse filer og mapper er udelukket fra versionskontrol:

| Fil/Mappe               | Hvorfor ignoreres det?                          |
| ----------------------- | ----------------------------------------------- |
| `.venv/`                | Lokalt virtuelt miljø – unikt for hver udvikler |
| `__pycache__/`, `*.pyc` | Python kompilerede filer – auto-genereret       |
| `.env`                  | Indeholder følsomme API-nøgler                  |
| `.idea/`                | PyCharm IDE-specifikke indstillinger            |

---

## 🧪 Test

Ingen tests endnu!

---

## 📄 Licens

MIT License – brug, kopier og bidrag frit.


