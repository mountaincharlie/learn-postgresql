import psycopg2


# connecting the chinook db (just by name cos we dont have any credentials)
connection = psycopg2.connect(database="chinook")

# building the cursor object for sorting through db info
cursor = connection.cursor()

# EXECUTING THE QUERIES
# Query 1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select "Name" column from "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only from "Queen" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only by "ArtistId" #51 from "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - trying to select all where "Name" is "Test" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["test"])


# fetching multiple results from the cursor
results = cursor.fetchall()

# fetching a single result
# results = cursor.fetchone()

# closing the connection
connection.close()

# printing the fetched results
for result in results:
    print(result)
