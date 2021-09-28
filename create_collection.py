#!/usr/bin/python3

from pymongo import MongoClient

etudiants = [ 
	{'nom': 'Jean', 'prenom' : 'Alice', 'ville':'Mons', 'option':'IG', 'notes' :[14,11,17]},
  	{'nom': 'Jacques', 'prenom' : 'Alicia', 'ville':'Charleroi', 'option':'Elec', 'notes' :[16, 12,10]},
	{'nom': 'Paul', 'prenom' : 'Lionel', 'ville':'Mons', 'option':'Meca', 'notes' :[15, 13,18]},
  	{'nom': 'Julien', 'prenom' : 'Marc', 'ville':'Charleroi', 'option':'IG', 'notes' :[18, 19, 16]},
	{'nom': 'Miles', 'prenom' : 'Lisa', 'ville':'Mons', 'option':'Meca', 'notes' :[17, 15, 19]},
  	{'nom': 'Milenium', 'prenom' : 'Lucas', 'ville':'Mons', 'option':'Meca', 'notes' :[11, 19, 18]}

]

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.database_tp
    
    db.etudiants.insert_many(etudiants)