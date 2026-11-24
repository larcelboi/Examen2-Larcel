from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

import config

uri = config.MONGODB_URI

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connexion réussie")
    client.close()

except OperationFailure as e:
    print("Erreur d'authentification ou de droits :", e)
except ConnectionFailure as e:
    print("Cluster injoignable (adresse IP autorisée dans Network Access ?) :", e)
