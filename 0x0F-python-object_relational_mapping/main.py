#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String(50))
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    
    def __init__(self, ssn, firstname, lastname, age, gender):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        
        
    def __repr__(self):
        return f"({self.ssh}) {self.firstname} {self.lastname} {self.age} {self.gender}"
    

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(111, "Tony", "NTAHE", 26, "m")
session.add(person)
session.commit()

p1 = Person(112, "ABAVANDIMWE", "Sapiens", 25, "m")
session.add(p1)

p2 = Person(113, "Boris", "NGABO", 25, "m")
session.add(person)

p3 = Person(114, "Young", "Gio", 24, "f")
session.add(p3)
session.commit()

result = session.query(Person).filter(Person.ssn == 112)
print(result)
