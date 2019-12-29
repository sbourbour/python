## Requirements for cassandradata.py

This service requires Apache Cassandra. 
The Cassandra database will need to hold a table containing the items and the prices.

You may install Java, Python, and Cassandra by following the instructions provided here:

    https://www.how2shout.com/how-to/install-apache-cassandra-on-windows-10-8-7-without-datastax.html

(make sure you download Cassandra 3.11.4)
    http://www.apache.org/dyn/closer.lua/cassandra/3.11.4/apache-cassandra-3.11.4-bin.tar.gz
 
The latest Python at this time is 3.8.1

    https://www.python.org/downloads/

In the Python installation box, just check the box to add Python to PATH.
 
## Cassandra driver for Python

    https://docs.datastax.com/en/developer/python-driver/3.20/installation/ 

## Cassandra keyspace and table

Once Cassandra is running, you may create the keyspace and table using the cqlsh command line interface.

    C:\>cd C:\Users\Owner\apache-cassandra-3.11.4\bin

    C:\Users\Owner\apache-cassandra-3.11.4\bin>cqlsh


## Cassandra Keyspace

    CREATE KEYSPACE shahriar WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

## Cassandra Table

    CREATE TABLE shahriar.person (
	   firstName text,
	   lastName text,
	   birthdate text,
	   gender text,
	   attributesjson text,
	   PRIMARY KEY(lastName, firstName, birthdate, gender)
	   );
   

