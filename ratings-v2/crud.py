"""CRUD Operations"""

from model import db, User, Movie, Rating, connect_to_db
import datetime

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, 
                  overview=overview, 
                  release_date=release_date,
                  poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Return all movies"""

    return Movie.query.all()

def create_rating(user, movie, score):
    """Create and return a new movie rating"""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating

def get_movie_by_id(movie_id):
    """Get a Movie by ID"""  


    return Movie.query.get(movie_id)

def get_users():
    """Return all users"""

    return User.query.all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)

