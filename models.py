from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    interests = db.Column(db.Text)
    # birthday = db.Column(db.DateTime)
    # nationalid = db.Column(db.String())
    # address = db.Column(db.Text)
    # phone = db.Column(db.String())
    # facebook = db.Column(db.String())
    # work_school = db.Column(db.Text)
    # language = db.Column(db.String())
    # lang_prof = db.Column(db.String())
    # emergency_contact = db.Column(db.Text)
    # comments = db.Column(db.Text)

    def __repr__(self):
        return 'Email {}'.format(self.email)
        
class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    date = db.Column(db.DateTime)
    starttime = db.Column(db.String())
    endtime = db.Column(db.String())
    email = db.Column(db.String(), db.ForeignKey('users.email'))
    content = db.Column(db.Text)
    interests = db.Column(db.Text)
    
    def __repr__(self):
        return 'id {}'.format(self.id)
        
class Amber(db.Model):
    __tablename__ = 'amber'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    seen = db.Column(db.Text)    
    date = db.Column(db.DateTime)