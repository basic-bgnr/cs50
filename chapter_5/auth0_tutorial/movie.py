from sqlalchemy import Column, Integer, Numeric, String, Date, Table, ForeignKey
from base import Base

from actor import Actor
from sqlalchemy.orm import relationship

movie_actor_association = Table(
        'movie_actors', Base.metadata,
        Column('movie_id', Integer, ForeignKey('movies.id')),
        Column('actor_id', Integer, ForeignKey('actors.id'))
        )

class Movie(Base):
    __tablename__ ='movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    actors = relationship('Actor', secondary=movie_actor_association)


    def __init__(self, title, release_date): 
        self.title = title
        self.release_date = release_date


