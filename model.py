from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
import seed

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
    """docstring for User"""
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = False)
    password = Column(String(64), nullable = True)
    gender = Column(String(2), nullable = True)
    occupation = Column(String(80), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)

class Movie(Base):
    """docstring for Movie"""
    __tablename__ = "Movies"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = True)
    url = Column(String(150), nullable = True)
    released_at = Column(Date, nullable = True)
    imdb_url = Column(String(150), nullable = True)

class Rating(Base):
    """docstring for Rating"""
    __tablename__ = "Ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    movie_id = Column(Integer, nullable = False)
    rating = Column(Integer, nullable = True)
    timestamp = Column(DateTime, nullable = True)

    user = relationship("User", backref=backref("ratings", order_by=id))

### End class declarations
def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)
    Base.metadata.create_all(ENGINE)

    return Session()


def main():
    
    # session = ""

    seed.main(session)

    session.commit()

if __name__ == "__main__":
    main()
