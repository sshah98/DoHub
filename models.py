from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    interests = db.Column(db.Text)

    def __repr__(self):
        return 'Email {}'.format(self.email)
        
class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    datetime = db.Column(db.DateTime)
    email = db.Column(db.String(), db.ForeignKey('users.email'))
    content = db.Column(db.Text)
    interests = db.Column(db.Text)
    
    def __repr__(self):
        return 'id {}'.format(self.id)