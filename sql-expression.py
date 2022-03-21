# using SQLAlchemy with expression language commands
from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost (hence '///') "chinook" db
db = create_engine("postgresql:///chinook")

# collection of table objects and associated data
meta = MetaData(db)

# SETTING UP THE TABLE VARS
# create variable for "Artist" table (with the Table import, the tabel name and its data)
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String) 
)
# "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId")) 
)
# "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# connecting the db (saving it into a variable 'connection')
with db.connect() as connection:
    # THE QUERIES
    # Query 1 - select all records from "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select "Name" column from "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only from "Queen" from "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by "ArtistId" #51 from "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only by "ArtistId" #51 from "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is "Queen" from "Track" table
    # select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    n = 0
    for result in results:
        n+= 1
        print(result)
    print("Number of results: ", n)
