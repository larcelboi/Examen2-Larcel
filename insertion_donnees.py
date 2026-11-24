from datetime import datetime, timedelta, timezone
from random import randint
import random

from pymongo import MongoClient

import config

client = MongoClient(config.MONGODB_URI, serverSelectionTimeoutMS=5000, tz_aware=True)
db = client[config.MONGODB_BASE]


# Supprimer toutes les collections existantes
for nom in (
    "stations",
    "depots",
    "etudiants",
    "casiers",
    "telephone_oubliees",
    "occupations",
):
    db.drop_collection(nom)

STATION = "point-recharge-01"
maintenant = datetime.now()

db.stations.insert_one({"_id": STATION, "nom": "Point Recharge de la bibliothèque"})

jasmine, sophia, shanys = [
    {"_id": "1234567", "nom": "Jasmine", "Telephone": "Iphone 13"},
    {"_id": "9876543", "nom": "Sophia", "Telephone": "Iphone 15"},
    {"_id": "3216549", "nom": "Shanys", "Telephone": "Iphone 14"},
]


def depot(code, date_retour=None):
    return {
        "station_id": STATION,
        "code_hache": code,
        "date_retour": date_retour,
    }


hier = maintenant - timedelta(days=1)

random_etat = random.choice([True, False])
etat_off = False
# la station et ses 8 casiers, avec au moins un casier de chaque état ;
db.casiers.insert_many(
    [
        {
            "_id": f"caiser00{i}",
            "numero_casier": f"{i}",
            "station_id": "point-recharge-01",
            "code_hache": "9090",
            "date_retour": None,  # n'a pas encore été retourné
            "etudiant_id": f"{random.shuffle([jasmine['_id'], sophia['_id'], shanys['_id']])}",
            "etat": {
                "libre": bool(i == 1 or i == 5),
                "en_recharge": bool(i == 2 or i == 6),
                "chargé": bool(i == 3 or i == 7),
                "panne": bool(i == 4 or i == 8),
            },
        }
        for i in range(1, 9)
    ]
)


# 3 étudiants
for i in (jasmine, sophia, shanys):
    db.etudiants.insert_one(i)


n = 15
deniere_heures = maintenant - timedelta(hours=4)

# 16 lectures d'occupation, une aux 15 minutes pendant les 4 dernières heures ;

documentsOcc = []
db.create_collection(
    "occupations",
    timeseries={
        "timeField": "horodatage",
        "metaField": "station_id",
        "granularity": "minutes",
    },
)

for i in range(1, 15):
    nouv_heure = deniere_heures + timedelta(minutes=n)
    documentsOcc.append(
        {
            "horodatage": nouv_heure,
            "station_id": STATION,
            "nombre_casier_occ": round(random.uniform(1, 8)),
        }
    )
db.occupations.insert_many(documentsOcc)


documents = []
# Insérer plusieurs donnees dans la collection depots
hiers = maintenant - timedelta(days=1)
recuperer = None

for i in range(1, 6):
    if i < 3:
        horodatage = maintenant
        print(horodatage)
    elif i == 5:
        recuperer = horodatage
    else:
        horodatage = hiers

    documents.append(
        {
            "horodatage": horodatage,
            "station_id": "point-recharge-01",
            "code_hache": "9090",
            "date_retour": recuperer,
            "etudiant_id": "1234567",
            "casier_id": f"casieer00{round(random.uniform(1, 8))}",
        }
    )


db.depots.insert_many(documents)
