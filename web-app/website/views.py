
from os import error
from flask import Blueprint, render_template, request, redirect
from sqlalchemy import text
from flask.helpers import url_for

from .model import db, Song, Artist, Band, Singer, Feature, Album, Genre, Rating, Created, Featured, Produce_a, Song_fb

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

        if song_name and song_length:
            record = Song(song_name, song_length)
            db.session.add(record)
            db.session.commit()
            return render_template('song_feedback.html', value=True)
        else:                                    
            return render_template('song_feedback.html', value=False)
    return render_template('song.html')


@views.route('/artist', methods=['POST', 'GET'])
def artist():  
    if request.method == 'POST':
        artist_name = request.form.get('name')

        if artist_name:
            record = Artist(artist_name)
            db.session.add(record)
            db.session.commit()
            return render_template('artist_feedback.html' ,value=True)   
        else:                                      
            return render_template('artist_feedback.html', value=False)
    return render_template('artist.html')


@views.route('/band', methods=['POST', 'GET'])
def band():  
    if request.method == 'POST':
        band_name = request.form.get('name')
        band_form_year = request.form.get('year')

        if band_name and band_form_year:
            record = Band(band_name, band_form_year)
            db.session.add(record)
            db.session.commit()
            return render_template('band_feedback.html', value=True)            
        else:                                      
            return render_template('band_feedback.html', value=False)
    return render_template('band.html')



@views.route('/singer', methods=['POST', 'GET'])
def singer():  
    if request.method == 'POST':
        singer_name = request.form.get('name')
        singer_birth_year = request.form.get('year')

        if singer_name and singer_birth_year:
            record = Singer(singer_name, singer_birth_year)
            db.session.add(record)
            db.session.commit()
            return render_template('singer_feedback.html', value=True)
        else:                                     
            return render_template('singer_feedback.html', value=False)
    return render_template('singer.html')


@views.route('/album', methods=['POST', 'GET'])
def album():  
    if request.method == 'POST':
        numTracks = request.form.get("number")
        album_name = request.form.get('name')

        if numTracks and album_name:
            record = Album(numTracks, album_name)
            db.session.add(record)
            db.session.commit()
            return render_template('album_feedback.html', value=True)       
        else:                                      
            return render_template('album_feedback.html', value=False)
    return render_template('album.html')




@views.route('/genre', methods=['POST', 'GET'])
def genre():  
    if request.method == 'POST':
        genre_name = request.form.get('name')

        if genre_name:
            record = Genre(genre_name)
            db.session.add(record)
            db.session.commit()
            return render_template('genre_feedback.html', value=True)
        else:                                      
            return render_template('genre_feedback.html', value=True)
    return render_template('genre.html')



@views.route('/rating', methods=['POST', 'GET'])
def rating():  
    if request.method == 'POST':
        stars = request.form.get('stars')

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
        song = Song.query.filter_by(song_name=name)

        if song:
            id = request.form.get('sid')
            record = Feature(id)
            db.session.add(record)
            db.session.commit()
            return render_template('feature_feedback.html', value=True)
        else:                                      
            return render_template('feature_feedback.html', value=False)
    return render_template('feature.html')



@views.route('/created', methods=['POST', 'GET'])
def created():  
    if request.method == 'POST':
        song_id = request.form.get('song')
        artist_id = request.form.get('artist')
        release_year = request.form.get('ry')

        if song_id and artist_id and release_year:
            new_created_song = Created(song_id, artist_id, release_year)
            db.session.add(new_created_song)
            db.session.commit()
            return render_template('created_feedback.html', value=True)

        else:                                    
            return render_template('created_feedback.html', value=False)
    return render_template('created.html')


@views.route('/produce', methods=['POST', 'GET'])
def produce():  
    if request.method == 'POST':
        artist_id = request.form.get('artist')
        album_id = request.form.get('album')
        release_year = request.form.get('ry')

        if artist_id and album_id and release_year:
            new_produced_song = Produce_a(artist_id, album_id, release_year)
            db.session.add(new_produced_song)
            db.session.commit()

            return redirect('produce_feedback.html', value=True)
        else:                                      
            return render_template('produce_feedback.html', value=False)
    return render_template('produce.html')


@views.route('/song_fb', methods=['POST', 'GET'])
def song_fb():  
    if request.method == 'POST':
        song_id = request.form.get('song')
        feedback_id = request.form.get('fb')
        reference = request.form.get('reference')

        if song_id and feedback_id and reference:
            new_feedback_song = Song_fb(song_id, feedback_id, reference)
            print(new_feedback_song)
            db.session.add(new_feedback_song)
            db.session.commit()
            return render_template('song_fb_feedback.html', value=True)
        else:                                      
            return render_template('song_fb_feedback.html', value=False)
    return render_template('song_fb.html')


@views.route('/featured', methods=['POST', 'GET'])
def featured():  
    if request.method == 'POST':
        artist_id = request.form.get('artist')
        sid = request.form.get('song')
        artist_count = request.form.get('ac')

        if artist_id and sid and artist_count:
            new_featured_song = Featured(artist_id, sid, artist_count)
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
  
