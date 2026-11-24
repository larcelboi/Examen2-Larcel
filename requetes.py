import random
from datetime import datetime, timedelta, timezone

from pymongo import MongoClient

import config

client = MongoClient(config.MONGODB_URI, serverSelectionTimeoutMS=5000, tz_aware=True)
db = client[config.MONGODB_BASE]


STATION = "point-recharge-01"

maintenant = datetime.now(timezone.utc)
minuit = datetime.now(config.FUSEAU_LOCAL).replace(
    hour=0, minute=0, second=0, microsecond=0
)

# Q1
n = 10

telephone_oublier = db.depots.find(
    {"horodatage": {"$gte": minuit}, "date_retour": None},
    {"etudiant_id": 1, "casier_id": 1, "date_retour": 1},
).sort({"horodatage": 1})

for i in telephone_oublier:
    print(i)

print()
# Q2

# Trouver un casier qui est libre
casiers_libres = db.casiers.find({"etat.libre": True, "date_retour": None})
for i in casiers_libres:
    print(i)

print()
# obtenir un casier libre parmis les choix founissent
casier_libre = db.casiers.find_one({"_id": "caiser005"})
print(casier_libre)

# Insérer
