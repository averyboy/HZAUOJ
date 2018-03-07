from flask_sqlalchemy import SQLAlchemy
from . import db
class Role(db.Model):
    __tablename__='roels'
    id=Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model)：
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    password=db.Column(db.String(100),default='')
    username=db.Column(db.String(100),unique=True,index=True)
    roleid=db.Column(db.Integer)
    def __repr__(self):
        return '<User %r>' % self.username