from tweet.database import db
# from sqlalchemy import func 
# import datetime

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(255),nullable=False)  
    email = db.Column(db.String(225),nullable=False)
    username = db.Column(db.String(225),nullable=False)
    password = db.Column(db.String(20),nullable=False)
    # this informs python that you are creating a connection between table 1 and table 2
    tweets = db.relationship("Tweet", cascade='all,delete', backref='user')

class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer,primary_key=True)
    msg = db.Column(db.String(255),nullable=False)  
    # posted_at = db.Column(db.DateTime, nullable=False,default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

