from . import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True, nullable = False)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    user = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    gen = db.Column(db.String(6))
    bio = db.Column(db.String(200))
    img = db.Column(db.String(256))
    date = db.Column(db.DateTime)
    
    def __init__(self, fname, lname, user, age, gen, bio, img, date):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.user = user
        self.age = age
        self.gen = gen
        self.bio = bio
        self.img = img
        self.date = date

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.user)

