from os import error
from flask import Blueprint, render_template, request, flash, redirect
from sqlalchemy import text
from flask.helpers import url_for

#from website.app import AddRecord
from .model import db, Song

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
        print(song_name, song_length)

        if song_name and song_length:
            record = Song(song_name, song_length)
            db.session.add(record)
            db.session.commit()

            flash(f"{record} sucessfully added!", category='success')
            return redirect(url_for('views.home'))
        else:
            return render_template('song.htm')
    return render_template('song.htm')

  
