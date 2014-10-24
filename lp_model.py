from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
import sys
import csv

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
    user_id = Column(Integer, nullable = False)
    movie_id = Column(Integer, nullable = False)
    movie_rating = Column(Integer, nullable = True)
    timestamp = Column(DateTime, nullable = True)

### End class declarations

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

def load_rating_data(filename, session):

    print (0, "file name = ", filename)

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter ='\t')
        try:
            for row in reader:
                print (0, "row = " , row)
                new_row = row.split()
                print (0.0, "new_row = ", new_row)
                user_id, movie_id, movie_rating, timestamp = new_row
                rating = Rating(
                    user_id=user_id, 
                    movie_id=movie_id,
                    movie_rating=movie_rating, 
                    timestamp=timestamp)
                session.add(rating)
            
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))   

def load_movie_data(filename, session):
    print (0, "file name = ", filename)

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter ='|')
        try:
            for row in reader:
                movie_id, name, released_at, url, imdb_url = row[:5]
                movie = Movie(
                    id = movie_id,
                    name=name, 
                    released_at=released_at, 
                    url=url, 
                    imdb_url=imdb_url)
                session.add(movie)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))   

def load_user_data(filename, session):
    print (0, "file name = ", filename)

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter ='|')
        try:
            for row in reader:
                user_id, age, gender, occupation, zipcode = row[0:]
                user = User(
                    id = user_id,
                    age=age, 
                    gender=gender, 
                    occupation=occupation, 
                    zipcode=zipcode)
                session.add(user)
            
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))   

def main():
    
    # session = ""
    session = connect()
    Base.metadata.create_all(ENGINE)

    ratings = './seed_data/lp_u.data'
    movies = './seed_data/lp_u.item'
    users = './seed_data/lp_u.user'

    load_rating_data(ratings, session)
    load_movie_data(movies, session)
    load_user_data(users, session)

    session.commit()

if __name__ == "__main__":
    main()
