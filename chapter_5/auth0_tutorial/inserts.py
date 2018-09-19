from datetime import date

from actor import Actor
from base import Session, engine, Base

from contact_details import ContactDetails
from movie import Movie

from stuntmen import StuntMan

Base.metadata.create_all(engine)


session = Session()

#create movies
bourne_identity = Movie('The Bourne Identity', date(2002, 10, 11))
furious_7 = Movie('Furious 7', date(2001, 10, 2))

# create actors

matt_damon = Actor('Matt Damon', date(1970, 10, 8))
dwayne_johnson = Actor('Dwayne Johnson', date(1972, 10, 10))


#adding actors to movie
bourne_identity.actors = [matt_damon]
furious_7.actors = [dwayne_johnson, matt_damon]

matt_contact = ContactDetails('23-12323', 'kathmandu', matt_damon)
dwayne_contact = ContactDetails('234-125545', 'lalitpur', dwayne_johnson)
dwayne_contact2 =ContactDetails('234-125545', 'chabahil', dwayne_johnson)


matt_stuntman = StuntMan('John Doe', True, matt_damon)
dwayne_stuntman = StuntMan('John Roe', True, dwayne_johnson)

session.add(bourne_identity)
session.add(furious_7)


session.add(matt_contact)
session.add(dwayne_contact)
session.add(dwayne_contact2)


session.add(matt_stuntman)
session.add(dwayne_stuntman)


session.commit()
session.close()


