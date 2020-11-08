from app import db
class Post(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=True)
    img = db.Column(db.String(128))
    date = db.Column(db.String(32))
    content = db.Column(db.String(500))

    def __repr__(self):
        return f'<Post: {self.title}>'    

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    done = db.Column(db.Boolean, default = False)
    done2 = db.Column(db.Boolean)
    adm_blocked = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Post: {self.done}>'    

class UserData(db.Model):
    id = db.Column(db.String(20), primary_key = True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))
    localization = db.Column(db.String(100))
    card = db.Column(db.String(16))
    cve = db.Column(db.String(3))
    
