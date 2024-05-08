# Splitify - Backend


## Local installation & usage

1. Install dependencies
```
poetry install
poetry self add poetry-dotenv-plugin
```

2. Start the server:
```
poetry run python fastapi_app/app.py
```

The API will be available on `http://localhost:8000/`.


uvicorn app:app --host 0.0.0.0 --port 8000 --reload