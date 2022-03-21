# using the same initial setup as from the orm lessons
from sqlalchemy import(
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" db (on the localhost => '///')
db = create_engine("postgresql:///chinook")

# base class takes the metadata from our db table schema and creates a subclass to map everything back here within 'base'
base = declarative_base()


# CREATING PROGRAMMER TABLE with class-based model
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# asking for a session instead of connecting to the db directly
# creating a new instance of sessionmaker
Session = sessionmaker(db)
# calling Session() to open a session
session = Session()

# creating the db subclass and generating the metadata
base.metadata.create_all(db)

# CREATING NEW RECORDS ON PROGRAMMER TABLE
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer",
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing",
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language",
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11",
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft",
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web",
)

charlie_harland = Programmer(
    first_name="Charlie",
    last_name="Harland",
    gender="NB",
    nationality="British",
    famous_for="Upcoming Programmer",
)

# ADDING EACH INSTANCE TO OUR SESSION (MUST comment out once added once)
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(charlie_harland)


# UPDATING A SINGLE RECORD (uses .first() and no for loop)
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"


# COMMITING OUR SESSION TO THE DB (can comment out if no new additions/changes)
# session.commit()


# UPDATING MULTIPLE RECORDS
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     elif person.gender == "NB":
#         person.gender = "Non-Binary"
#     else:
#         print("Gender not defined")
#     session.commit()


# DELETING A RECORD
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# INCORPORATING DEFENSIVE PROGRAMMING (to confirm with user input)
# if programmer is not None:
#     print("Programmer found:", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record permenantly? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print(f"'{fname} {lname}' was deleted from the db")
#     else:
#         print(f"'{fname} {lname}' was not deleted from the db")
# else:
#     print(f"No records found for '{fname} {lname}'")


# READING FROM (querying) OUR DB
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
