from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    haircolor = Column(String)
    eyecolor = Column(String)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    climate = Column(String)
    

class Favorites(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    character = relationship(Character)
    character_id = Column(Integer, ForeignKey("character.id"), nullable=True)
    planet = relationship(Planet)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey("user.id"))c

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }