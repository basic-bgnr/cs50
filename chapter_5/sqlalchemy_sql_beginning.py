from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


    def __repr__(self):
        return f"{self.username}"
db.create_all()


user_1 = User(username='admin', email='admin123')
user_2 = User(username='user', email='123')

db.session.add(user_1)
db.session.add(user_2)

db.session.commit()


