
#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.database_tp

    n_etudiants = db.etudiants.find({'option':'IG'}).count()

    print("Il y a {} etudiants en option IG".format(n_etudiants))
