import model   # if you do it this way, model.User, model.connect
import csv
import sys
from model import User, Movie, Rating   # if you do it this way, User, connect
from datetime import datetime
import re

# you need to pip install arrow for this to work


def load_users(session):

    filename = './seed_data/u.user'

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

def load_movies(session):

    filename = './seed_data/u.item'
    
    print (0, "file name = ", filename)

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter ='|')
        try:
            for row in reader:
                movie_id, name, released_at, url, imdb_url = row[:5]
                if released_at != "":
                    released_at = datetime.strptime(released_at, "%d-%b-%Y")
                else:
                    released_at = None
                name = parse_movie_title(name)
                movie = Movie(
                    id = movie_id,
                    name=name, 
                    released_at=released_at, 
                    url=url, 
                    imdb_url=imdb_url)
                session.add(movie)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))   

def load_ratings(session):

    filename = './seed_data/u.data'
    
    print (0, "file name = ", filename)

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter ='\t')
        try:
            for row in reader:
                user_id, movie_id, movie_rating, timestamp = row
                rating = Rating(
                    user_id=user_id, 
                    movie_id=movie_id, 
                    movie_rating=movie_rating, 
                    timestamp=datetime.fromtimestamp(float(timestamp)))
                session.add(rating)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))  

def parse_movie_title(name):
    
    name = re.sub('\(\d+\)', '', name).rstrip()
    name = name.decode("latin-1")
    
    return name


def main(session):
    # You'll call each of the load_* functions with the session as an argument

    load_users(session)
    load_movies(session)
    load_ratings(session)

    session.commit()

if __name__ == "__main__":
    s= model.connect()
    main(s)
