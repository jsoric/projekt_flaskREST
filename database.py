from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Register(db.Model):
    __tablename__ = 'register'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)
    spol = db.Column(db.String(50))
    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(self.id, self.name, self.surname, self.email, self.password, self.spol)

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.Text)
    def __repr__(self):
        return '{}, {}, {}'.format(self.id, self.email, self.password)