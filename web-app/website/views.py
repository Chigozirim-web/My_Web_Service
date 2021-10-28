from os import error
from flask import Blueprint, render_template, request, flash, redirect
from sqlalchemy import text
from flask.helpers import url_for

from .model import db, Song  #...also import all other classes too from models.py ie Artist etc...

views = Blueprint('views', __name__)

@views.route('/')
def home():
   return render_template('index.html')

@views.route('/imprint')
def imprint():
    return render_template('imprint.html')


@views.route('/song', methods=['POST', 'GET'])
def song():  
    if request.method == 'POST':
        song_name = request.form.get('name')
        song_length = request.form.get('length')

        if song_name and song_length:
            record = Song(song_name, song_length)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('song.htm')
    return render_template('song.htm')


@views.route('/artist', methods=['POST', 'GET'])
def artist():  
    if request.method == 'POST':
        artist_name = request.form.get('name')


        if artist_name:
            record = Artist(artist_name)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('artist.htm')
    return render_template('artist.htm')

@views.route('/band', methods=['POST', 'GET'])
def band():  
    if request.method == 'POST':
        band_name = request.form.get('name')
        band_form_year = request.form.get('year')

        if band_name and band_form_year:
            record = Band(band_name, band_form_year)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('band.htm')
    return render_template('band.htm')



@views.route('/singer', methods=['POST', 'GET'])
def singer():  
    if request.method == 'POST':
        singer_name = request.form.get('name')
        singer_birth_year = request.form.get('year')

        if singer_name and singer_birth_year:
            record = Singer(singer_name, singer_birth_year)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('singer.htm')
    return render_template('singer.htm')


@views.route('/album', methods=['POST', 'GET'])
def album():  
    if request.method == 'POST':
        numTracks = request.form.get("number")
        album_name = request.form.get('name')

        if numTracks and album_name:
            record = Album(numTracks, album_name)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('album.htm')
    return render_template('album.htm')




@views.route('/genre', methods=['POST', 'GET'])
def genre():  
    if request.method == 'POST':
        genre_name = request.form.get('name')

        if genre_name:
            record = Genre(genre_name)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('genre.htm')
    return render_template('genre.htm')


@views.route('/genre', methods=['POST', 'GET'])
def rating():  
    if request.method == 'POST':
        stars = request.form.get('stars')

        if stars:
            record = Rating(stars)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))  #if input was correct go back to maintenance page
        else:                                      # so create a route for maintenance too btw
            return render_template('rating.htm')
    return render_template('rating.htm')

def check():  # just error checking if the database connected
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
  
