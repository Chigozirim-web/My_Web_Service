
from os import error
from flask import Blueprint, render_template, request, redirect
from sqlalchemy import text, exc
from flask.helpers import url_for

from .model import db, Song, Artist, Band, Singer, Feature, Album, Genre, Rating, Created, Featured, Produce_a, Song_fb

#BELOW:
#error 1 or 2 means an input is missing
#error 3 means successful (yes it's kinda misleading, but didn't want to change variable)
#error 4 means Integrity error (input already exists)

views = Blueprint('views', __name__)

@views.route('/')
def home():
   return render_template('index.html')

@views.route('/imprint')
def imprint():
    return render_template('imprint.html')

@views.route('/maintenance')
def maintenance():
   return render_template('maintenance.html')

@views.route('/song', methods=['POST', 'GET'])
def song():  
    if request.method == 'POST':
        song_name = request.form.get('name')
        song_length = request.form.get('length')
        if not song_name:
            error = 1
        if not song_length:
            error = 2
        if song_name and song_length:
            try:
                record = Song(song_name, song_length)
                db.session.add(record)
                db.session.commit()
                error = 3
                return render_template('song_feedback.html', error=error)
            except exc.IntegrityError:
                error = 4
                return render_template('song_feedback.html', error=error)
        else:                                    
            return render_template('song_feedback.html', error=error)
    return render_template('song.html')


@views.route('/artist', methods=['POST', 'GET'])
def artist():  
    if request.method == 'POST':
        artist_name = request.form.get('name')
        if not artist_name:
            error = 1                                              
            return render_template('artist_feedback.html', error=error)
        else:
            try:
                record = Artist(artist_name)
                db.session.add(record)
                db.session.commit()
                error = 3
                return render_template('artist_feedback.html', error=error)
            except exc.IntegrityError:
                error = 4
                return render_template('artist_feedback.html', error=error)
    return render_template('artist.html')


@views.route('/band', methods=['POST', 'GET'])
def band():  
    if request.method == 'POST':
        band_name = request.form.get('name')
        band_form_year = request.form.get('year')

        if not band_name:
            error = 1
        if not band_form_year:
            error = 2
        if band_name and band_form_year:
            try:
                record = Band(band_name, band_form_year)
                db.session.add(record)
                db.session.commit()
                error = 3
                return render_template('band_feedback.html', error=error)
            except exc.IntegrityError:
                error = 4
                return render_template('band_feedback.html', error=error)
        else:                                    
            return render_template('band_feedback.html', error=error)
    return render_template('band.html')



@views.route('/singer', methods=['POST', 'GET'])
def singer():  
    if request.method == 'POST':
        singer_name = request.form.get('name')
        singer_birth_year = request.form.get('year')
        if not singer_name:
            error = 1
        if not singer_birth_year:
            error = 2
        if singer_name and singer_birth_year:
            try:
                record = Singer(singer_name, singer_birth_year)
                db.session.add(record)
                db.session.commit()
                error = 3
                return render_template('singer_feedback.html', error=error)
            except exc.IntegrityError:
                error = 4
                return render_template('singer_feedback.html', error=error)
        else:                                    
            return render_template('singer_feedback.html', error=error)
    return render_template('singer.html')



@views.route('/album', methods=['POST', 'GET'])
def album():  
    if request.method == 'POST':
        numTracks = request.form.get("length")
        album_name = request.form.get('name')

        if not numTracks:
            error = 1
        if not album_name:
            error = 2
        if numTracks and album_name:
            try:
                record = Album(numTracks, album_name)
                db.session.add(record)
                db.session.commit()
                error = 3
                return render_template('album_feedback.html', error=error)
            except exc.IntegrityError:
                error = 4
                return render_template('album_feedback.html', error=error)
        else:                                    
            return render_template('album_feedback.html', error=error)
    return render_template('album.html')



@views.route('/genre', methods=['POST', 'GET'])
def genre():  
    if request.method == 'POST':
        genre_name = request.form.get('name')
        
        if not genre_name:
            error = 1
            return render_template('genre_feedback.html', error=error)
        else:
            try:
                record = Genre(genre_name)
                db.session.add(record)
                db.session.commit()
                error = 3
                return render_template('genre_feedback.html', error=error)
            except exc.IntegrityError:
                error = 4
                return render_template('genre_feedback.html', error=error)                                     
    return render_template('genre.html')



@views.route('/rating', methods=['POST', 'GET'])
def rating():  
    if request.method == 'POST':
        stars = request.form.get('stars')
        #No integrity constraints here...
        if stars:
            record = Rating(stars)
            db.session.add(record)
            db.session.commit()
            return render_template('rating_feedback.html', value=True)
        else:                                      
            return render_template('rating_feedback.html', value=False)
    return render_template('rating.html')


@views.route('/feature', methods=['POST', 'GET'])
def feature():  
    if request.method == 'POST':
        name = request.form.get('name')
        sid = db.session.query(Song.id).filter_by(song_name=name)

        if sid:
            record = Feature(sid)
            db.session.add(record)
            db.session.commit()
            return render_template('feature_feedback.html', value=True)
        else:                                      
            return render_template('feature_feedback.html', value=False)
    return render_template('feature.html')

##RELATIONSHIP ROUTES

@views.route('/created', methods=['POST', 'GET'])
def created():  
    if request.method == 'POST':
        song = request.form.get('song')
        artist = request.form.get('artist')
        release_year = request.form.get('ry')

        s = db.session.query(Song.id).filter_by(song_name=song)
        ar = db.session.query(Artist.id).filter_by(artist_name=artist)

        if s and ar and release_year:
            new_created_song = Created(s, ar, release_year)
            db.session.add(new_created_song)
            db.session.commit()
            return render_template('created_feedback.html', value=True)

        else:                                    
            return render_template('created_feedback.html', value=False)
    return render_template('created.html')


@views.route('/produce', methods=['POST', 'GET'])
def produce():  
    if request.method == 'POST':
        artist = request.form.get('artist')
        album = request.form.get('album')
        release_year = request.form.get('ry')

        ar = db.session.query(Artist.id).filter_by(artist_name=artist)
        al = db.session.query(Album.id).filter_by(album_name=album)

        if ar and al and release_year:
            new_produced_album = Produce_a(ar, al, release_year)
            db.session.add(new_produced_album)
            db.session.commit()

            return redirect('produce_feedback.html', value=True)
        else:                                      
            return render_template('produce_feedback.html', value=False)
    return render_template('produce.html')


@views.route('/song_fb', methods=['POST', 'GET'])
def song_fb():  
    if request.method == 'POST':
        song = request.form.get('song')
        feed = request.form.get('fb')
        reference = request.form.get('reference')
        
        s = db.session.query(Song.id).filter_by(song_name=song)
        f = db.session.query(Rating.id).filter_by(stars=feed)

        if s and f and reference:
            new_feedback_song = Song_fb(s, f, reference)
            db.session.add(new_feedback_song)
            db.session.commit()
            return render_template('song_fb_feedback.html', value=True)
        else:                                      
            return render_template('song_fb_feedback.html', value=False)
    return render_template('song_fb.html')


@views.route('/featured', methods=['POST', 'GET'])
def featured():  
    if request.method == 'POST':
        artist = request.form.get('artist')
        song = request.form.get('song')
        artist_count = request.form.get('ac')
        
        ar = db.session.query(Artist.id).filter_by(artist_name=artist)
        s = db.session.query(Song.id).filter_by(song_name=song)

        if s and ar and artist_count:
            new_featured_song = Featured(ar, s, artist_count)
            db.session.add(new_featured_song)
            db.session.commit()
            return render_template('featured_feedback.html', value=True)    
        else:                                      
            return render_template('featured_feedback.html', value=False)
    return render_template('featured.html')


def check():  # just error checking if the database connected
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
  
