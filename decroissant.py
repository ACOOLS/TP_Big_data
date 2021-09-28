#!/usr/bin/python3

from pymongo import MongoClient, DESCENDING

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.database_tp

    etudiant = db.etudiants.find().sort("prenom", DESCENDING)

    for etu in etudiant:
        print('{0} {1}'.format(etu['nom'], 
            etu['prenom']))