from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI CI/CD Demo"
    environment: str = "local"
    version: str = "0.1.0"

settings = Settings()

app = FastAPI(title=settings.app_name, version=settings.version)


@app.get("/")
def read_root():
    return {
        "message": f"Hello from {settings.app_name}!",
        "env": settings.environment,
        "version": settings.version,
    }


@app.get("/health")
def health():
    return {"status": "ok"}
