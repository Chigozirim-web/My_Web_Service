from . import db


class Song(db.Model):
    __tablename__ = 'Song'
    __table_args__ = (db.UniqueConstraint('song_name'), )
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(20), unique=True)
    song_length = db.Column(db.Integer)

    def __init__(self, name, length):
        self.song_name = name
        self.song_length = length


class Artist(db.Model):
    __tablename__='Artist'
    id = db.Column (db.Integer, primary_key=True)
    artist_name = db.Column (db.String(128))
    __table_args__ = (db.UniqueConstraint('artist_name'), )

    def __init__(self, name):
        self.artist_name = name



class Band(db.Model):
    __tablename__='Band'
    __table_args__ = (db.UniqueConstraint('artist_name'), )
    id = db.Column (db.Integer, primary_key=True)
    artist_name = db.Column (db.String(128))
    form_year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.artist_name = name
        self.form_year = year



    
class Singer(db.Model):
    __tablename__='Singer'
    __table_args__ = (db.UniqueConstraint('artist_name'), )
    id = db.Column (db.Integer, primary_key=True)
    artist_name = db.Column (db.String(128))
    birth_year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.artist_name = name
        self.birth_year = year


class Album(db.Model):
    __tablename__ = 'Album'
    __table_args__ = (db.UniqueConstraint('album_name'), )
    id = db.Column (db.Integer, primary_key=True)
    numTracks = db.Column(db.Integer)
    album_name = db.Column(db.String(128))

    def __init__(self, number, name):
        self.numTracks = number
        self.album_name = name



class Genre(db.Model):
    __tablename__='Genre'
    __table_args__ = (db.UniqueConstraint('genre_name'), )
    id = db.Column (db.Integer, primary_key=True)
    genre_name = db.Column (db.String(20))  

    def __init__(self, name):
        self.genre_name = name


class Rating(db.Model):
    __tablename__ = 'Rating'
    id = db.Column (db.Integer, primary_key=True)
    stars = db.Column(db.Integer)

    def __init__(self, stars):
        self.stars = stars



class Feature(db.Model):  #ISA Song
    __tablename__ = 'Feature'
    song_id = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, sid):
        self.song_id = sid

    
    
# RELATIONSHIPS


class Created(db.Model):
    __tablename__ = 'created'
    song_id = db.Column (db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer)
    release_year = db.Column(db.Integer)

    def __init__(self, sid, aid, year):
        self.song_id = sid
        self.artist_id = aid
        self.release_year = year



class Produce_a(db.Model):
    __tablename__ = 'produce'
    artist_id = db.Column(db.Integer)
    album_id = db.Column(db.Integer, primary_key=True)
    release_year = db.Column(db.Integer)

    def __init__(self, aid, alid, year):
        self.artist_id = aid
        self.album_id = alid
        self.release_year = year
        

class Song_fb(db.Model):
    __tablename__ = 'song_fb'
    song_id = db.Column(db.Integer, primary_key=True)
    feedback_id = db.Column (db.Integer, primary_key=True)
    reference =  db.Column(db.String(128))

    def __init__(self, sid, fid, reference):
        self.song_id = sid
        self.feedback_id = fid
        self.reference = reference


class Featured(db.Model): 
    __tablename__ = 'featured'
    artist_id = db.Column (db.Integer)
    song_id = db.Column(db.Integer, primary_key=True)
    artist_count = db.Column(db.Integer)

    def __init__(self, aid, sid, num):
        self.artist_id = aid
        self.song_id = sid
        self.artist_count = num
    
