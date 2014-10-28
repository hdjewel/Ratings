from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session


engine = create_engine("sqlite:///ratings.db", echo=False)

session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))
Base = declarative_base()

Base.query = session.query_property()

### Class declarations go here
class User(Base):
    """docstring for User"""
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    gender = Column(String(2), nullable = True)
    occupation = Column(String(80), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)

class Movie(Base):
    """docstring for Movie"""
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = True)
    url = Column(String(150), nullable = True)
    released_at = Column(Date, nullable = True)
    imdb_url = Column(String(150), nullable = True)

class Rating(Base):
    """docstring for Rating"""
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable = False)
    movie_rating = Column(Integer, nullable = True)
    timestamp = Column(DateTime, nullable = True)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))

### End class declarations
def connect():

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)
    Base.metadata.create_all(ENGINE)

    return Session()

def main():
    pass
    # return session

if __name__ == "__main__":
    main()
