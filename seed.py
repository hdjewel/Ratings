import model
import csv
import sys

# you need to pip install arrow for this to work
import arrow

def load_ratings(filename, session):

    print (0, "file name = ", filename)

    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter ='\t')
        try:
            for row in reader:
                user_id, movie_id, rating, timestamp = row
                rating = Rating(
                    user_id=user_id, 
                    movie_id=movie_id, 
                    rating=rating, 
                    timestamp=timestamp)
                session.add(rating)
            
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))   

def load_movies(filename, session):
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

def load_users(filename, session):
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

def convert_timestamp(timestamp):
    date_and_time = arrow.get(timestamp)
    return date_and_time

def parse_movie_title(movie, name):
    tmp_name = name.split('(')
    title = tmp_name[1].rstrip()

    # add field to the movie table released_year (YYYY)

    # translate from latin-1 to unicode
    # title = row[3]
    # title = title.decode("latin-1")

def main(session):


    ratings = './seed_data/u.data'
    movies = './seed_data/u.item'
    users = './seed_data/u.user'
    # You'll call each of the load_* functions with the session as an argument
    load_users(users, session)
    load_movies(movies, session)
    load_ratings(ratings, session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
