import os
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv

RACINE = Path(__file__).resolve().parent
load_dotenv(RACINE / ".env")


def _lecture_env(nom: str) -> str:
    valeur = os.getenv(nom)
    if not valeur:
        raise RuntimeError(f"Variable d'environnement manquante : {nom}")
    return valeur


MONGODB_URI = _lecture_env("MONGODB_URI")
MONGODB_BASE = _lecture_env("MONGODB_BASE")
FUSEAU_LOCAL = ZoneInfo("America/Toronto")
