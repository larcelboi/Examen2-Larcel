from datetime import datetime, timedelta, timezone
from random import randint

from pymongo import MongoClient

import config

client = MongoClient(config.MONGODB_URI, serverSelectionTimeoutMS=5000, tz_aware=True)
db = client[config.MONGODB_BASE]


# Supprimer toutes les collections existantes
for nom in ("stations", "depots", "etudiants"):
    db.drop_collection(nom)

STATION = "point-recharge-01"
maintenant = datetime.now()

db.stations.insert_one({"_id": STATION, "nom": "Point Recharge de la bibliothèque"})

jasmine, sophia, shanys = [
    {"_id": "1234567", "nom": "Jasmine"},
    {"_id": "9876543", "nom": "Sophia"},
    {"_id": "3216549", "nom": "Shanys"},
]


def depot(code, date_retour=None):
    return {
        "station_id": STATION,
        "code_hache": code,
        "date_retour": date_retour,
    }


hier = maintenant - timedelta(days=1)
