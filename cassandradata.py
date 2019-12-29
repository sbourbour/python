from cassandra.cluster import Cluster
import json

cluster = Cluster()

# Connect to the keyspace shahriar in Cassandra
session = cluster.connect('shahriar')

# Insert statement with parameters
insertPerson = 'INSERT INTO shahriar.person \
    (firstName, lastName, birthdate, gender, attributesjson) \
    VALUES \
    (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')'

# Open and load file containing JSON
# Get first, last, DOB, gender
# Populate the params in the INSERT statement with values
# Note: json.dumps replaces single quotes with double
# Insert the row in the table

with open('person.json', 'r') as f:
    person = json.load(f)
    firstName = person['firstName'] 
    lastName = person['lastName']
    birthdate = person['birthdate']
    gender = person['gender']
    insertSQL = insertPerson.format(firstName, lastName, birthdate, gender, json.dumps(person))    
    session.execute(insertSQL)
   

