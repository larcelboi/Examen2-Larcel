# Modèle NoSQL de Point Recharge

> **Remarque :** Le courant de charge n'est pas enregistré, le Raspberry Pi l'utilise en temps réel pour changer l'état du casier. La couleur de la DEL n'est pas enregistrée non plus, car elle se déduit de l'état du casier.

## Collection `stations`
```python
station = {"_id": "point-recharge-01", "nom": "Point Recharge de la bibliothèque"}
```

## Collection `etudiants`

`_id` est le numéro unique de l'étudiant, c'est ce que l'étudiant entre au clavier.

```python
etudiant = {"_id": "1234567", "nom": "Jasmine"}
```

## Collection `depots`
```python
depot = {
    "station_id": "point-recharge-01",
    "code_hache": "9090",
    "date_retour": None,  # n'a pas encore été retourné
}
```