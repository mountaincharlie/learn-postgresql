from sqlalchemy import(
    create_engine, Column, Float, Integer, String, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" db (on the localhost => '///')
db = create_engine("postgresql:///chinook")

# base class takes the metadata from our db table schema and creates a subclass to map everything back here within 'base'
base = declarative_base()

# CREATING OUR TABLES IN CLASS-BASED MODEL with 'base' subclass
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# asking for a session instead of connecting to the db directly
# creating a new instance of sessionmaker
Session = sessionmaker(db)
# calling Session() to open a session
session = Session()

# creating the db subclass and generating the metadata
base.metadata.create_all(db)

# THE QUERIES
# Query 1 - select all records from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select "Name" column from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only from "Queen" from "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     if artist.Name == "Queen":
#         print(artist.ArtistId, artist.Name, sep=" | ")
# OR BETTER:
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only by "ArtistId" #51 from "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
