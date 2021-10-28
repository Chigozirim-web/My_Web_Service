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

def check():  # just error checking if the database connected
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
  
