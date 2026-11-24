# Modèle NoSQL de Point Recharge

> **Remarque :** Le courant de charge n'est pas enregistré, le Raspberry Pi l'utilise en temps réel pour changer l'état du casier. La couleur de la DEL n'est pas enregistrée non plus, car elle se déduit de l'état du casier.


## Collection `stations` Normale
```python
station = {
    "_id": "point-recharge-01",
    "nom": "Point Recharge de la bibliothèque",
    "casiers": [
        "casieer001",
        "casieer002",
        "casieer003",
        "casieer004",
        "casieer005",
        "casieer006",
        "casieer007",
        "casieer008",
    ],
}
```
J'ai utilisé un tableau parce que la station contient plusieurs casiers. Dans ce tableau j'ai fournit les _ids des 
Casiers pour faciliter de trouver l'information d'un casier spécifique dans la base de donnée

## Collection `etudiants` Normale
`_id` est le numéro unique de l'étudiant, c'est ce que l'étudiant entre au clavier.

```python
etudiant = {"_id": "1234567", "nom": "Jasmine", "Telehpone": "Iphone 13 "}
```
Ajouter une colonne simple Téléphone
Permet de quel téléphone l'apaprtient

## Collection `depots` Normale
```python
depot = {
    "station_id": "point-recharge-01",
    "code_hache": "9090",
    "date_retour": None,  # n'a pas encore été retourné,
    "etudiant_id": "1234567",
    "casier_id": "casieer001",
}
```
Ajotuer la colonne "etudiant_id" pour savoir qui à fait le dépot de son téléphone
"casier_id" permet de savoir dans quelle casier l'étudiant à fait le dépot

## Collection `Casier` Normale
```python
casier = {
    "_id" : "casieer001"
    "numero_casier" : "1"
    "station_id": "point-recharge-01",
    "code_hache": "9090",
    "date_retour": None,  # n'a pas encore été retourné
    "etudiant_id" : "1234567,
    "etat" : {
        "libre" : False,
        "en_recharge" : True,
        "chargé" : False,
        "panne" : False
    } 
    
}
```
Ajouter "etudiant_id" pour savoir quel étudiant utilise le casier.
L'ajout du sous document "etat" en {} est nécessaire, car cette état appartient au casier seulement. Son 
état est unique à lui même




## Collection `Occupation` Time series
```python
occupation = {
      timeseries={
        "timeField": "horodatage",
        "metaField": "casier_id",
        "granularity": "minutes",
    }
    "nombre_casier_occ" : 10
}
```
Cette collection est une time series car elle enregistre des données avec des dates à plusieurs reprises.
Les enregistrements ne s'efface pas. Ils se sauvegardent pour obtenir un résultat du nombre de casier occupés durant 
une journée spécifique