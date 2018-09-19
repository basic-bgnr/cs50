from base import Base, engine, Session
from movie import Movie

session = Session()


movies_query = session.query(Movie).all()

movies_query2 = Base.__text_signature__
for movie in movies_query:
    print(f'{movie.title} was released on {movie.release_date}')


