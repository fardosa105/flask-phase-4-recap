from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates


db = SQLAlchemy()

# association table
user_groups = db.Table('user_groups',
                       db.Column('user_id',db.Integer,db.ForeignKey('users.id'),primary_key=True),
                       db.Column('group_id',db.Integer,db.ForeignKey('groups.id'),primary_key=True))

 
class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    
    
    #adding serialization rules
    serialize_rules = ('-posts.user', '-groups.users',)
    
    
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False,unique=True)
    email = db.Column(db.String(225))
    
    # add relationship
    posts = db.relationship('Post',back_populates = 'user')
    groups = db.relationship('Group',secondary =user_groups,back_populates='users')
    
    # add validattions
    @validates('email')
    def valid_email(self,key,value):
        if '@'  not in value:
            raise ValueError('Your  Email address is missing "@"')
        return value 
    
       
    

class Post(db.Model,SerializerMixin):
    __tablename__= 'posts'
    
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(120))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    # add relationship
    user = db.relationship('User',back_populates = 'posts')    
    

class Group(db.Model):
    __tablename__ = 'groups'
    
    id =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String)      
    
    # add relationship
    users = db.relationship('User',secondary = user_groups,back_populates = 'groups')