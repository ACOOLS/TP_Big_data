
#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.database_tp

    n_etudiants = db.etudiants.find().count()

    print("Il y a {} etudiants".format(n_etudiants))
