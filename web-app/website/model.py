from . import db

class Song(db.Model):
    __tablename__ = 'Song'
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(20))
    song_length = db.Column(db.Integer)

    def __init__(self, name, length):
        self.song_name = name
        self.song_length = length


class Artist(db.Model):
    __tablename__='Artist'
    id = db.Column (db.Integer, primary_key=True)
    artist_name = db.Column (db.String(128))

    def __init__(self, name):
        self.artist_name = name



class Band(db.Model):
    __tablename__='Band'
    id = db.Column (db.Integer, primary_key=True)
    artist_name = db.Column (db.String(128))
    form_year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.artist_name = name
        self.form_year = year



    
class Singer(db.Model):
    __tablename__='Singer'
    id = db.Column (db.Integer, primary_key=True)
    artist_name = db.Column (db.String(128))
    birth_year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.artist_name = name
        self.birth_year = year


class Album(db.Model):
    __tablename__ = 'Album'
    id = db.Column (db.Integer, primary_key=True)
    numTracks = db.Column(db.Integer)
    album_name = db.Column(db.String(128))

    def __init__(self, number, name):
        self.numTracks = number
        self.album_name = name



class Genre(db.Model):
    __tablename__='Genre'
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



class Feature(db.Model):
    __tablename__ = 'Feature'
    song_id = db.Column(db.Integer, db.ForeignKey('Song.id'), primary_key=True)

    s = db.relationship('Song')
    
    
# RELATIONSHIPS


class Created(db.Model):
    __tablename__ = 'created'
    song_id = db.Column (db.Integer, db.ForeignKey('Song.id'), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    release_year = db.Column(db.Integer)

    def __init__(self, year):
        self.release_year = year

    s = db.relationship('Song')
    Ar = db.relationship('Artist')


class Produce_a(db.Model):
    __tablename__ = 'produce_a'
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    album_id = db.Column(db.Integer, db.ForeignKey('Album.id'), primary_key=True)
    release_year = db.Column(db.Integer)

    def __init__(self, year):
        self.release_year = year

    s = db.relationship('Song')
    al = db.relationship('Album')


class Song_fb(db.Model):
    __tablename__ = 'song_fb'
    song_id = db.Column(db.Integer, db.ForeignKey('Song.id'), primary_key=True)
    feedback_id = db.Column (db.Integer, db.ForeignKey('Rating.id'), primary_key=True)
    reference =  db.Column(db.String(128))

    def __init__(self, reference):
        self.reference = reference

    s = db.relationship('Song')
    r = db.relationship('Rating')


class Featured(db.Model): 
    __tablename__ = 'featured'
    artist_id = db.Column (db.Integer, db.ForeignKey('Artist.id'))
    sid = db.Column(db.Integer, db.ForeignKey('Feature.song_id'), primary_key=True)
    artist_count = db.column(db.Integer)

    #def __init__(self, num):
    #    self.artist_count = num
    
    ar = db.relationship('Artist')
    f = db.relationship('Feature')
