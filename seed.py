import model
import csv

# you need to pip install arrow for this to work
import arrow

def load_users(session):
    session.add(user)

def load_movies(session):
    session.add(movie)

def load_ratings(session):
    session.add(rating)

def convert_timestamp(timestamp):
    date_and_time = arrow.get(timestamp)
    return date_and_time

def parse_movie_title(movie.name):
    tmp_name = name.split('(')
    title = tmp_name[1].rstrip()

    # add field to the movie table released_year (YYYY)

    # translate from latin-1 to unicode
    # title = row[3]
    # title = title.decode("latin-1")

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
