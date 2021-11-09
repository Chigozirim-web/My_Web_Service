import csv

import sqlite3
from sqlite3 import Error

def main():
    open("musicdata.db", "w").close()
    my_connect = create_connection("musicdata.db")

    
    create_table_artist = """
    CREATE TABLE IF NOT EXISTS Artist(
    artist_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_Name VARCHAR(20)
    );
    """

    create_song_table = """
    CREATE TABLE IF NOT EXISTS Song(
    song_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(20) UNIQUE,
    song_length INTEGER,
    releaseYear INTEGER
    );
    """
    create_feedback_table = """
    CREATE TABLE IF NOT EXISTS Feedback(
    feedback_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    comment VARCHAR(256)
    );
    """
    create_rating_table = """
    CREATE TABLE IF NOT EXISTS Rating(
    feedback_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    stars INTEGER,
    FOREIGN KEY(feedback_ID)
    REFERENCES Feedback(feedback_ID)
    );
    """
    create_album_table = """
    CREATE TABLE IF NOT EXISTS Album(
    album_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    release_year INTEGER,
    numTracks INTEGER,
    title text
    );
    """
    create_table_genre = """
    CREATE TABLE IF NOT EXISTS Genre(
    genre_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    genre_name VARCHAR(20) UNIQUE
    );
    """
    create_artistBand_table = """
    CREATE TABLE IF NOT EXISTS Artist_Band(
    artist_ID INTEGER PRIMARY KEY,
    formationYear INTEGER,
    FOREIGN KEY(artist_ID)
    REFERENCES Artist(artist_ID)
    );
    """
    create_artistSinger_table = """
    CREATE TABLE IF NOT EXISTS Artist_Singer(
    artist_ID INTEGER PRIMARY KEY,
    birthYear INTEGER,
    FOREIGN KEY(artist_ID)
    REFERENCES Artist(artist_ID)
    );
    """
    create_table_created = """
    CREATE TABLE IF NOT EXISTS created(
    song_ID INTEGER,
    artist_ID INTEGER ,
    PRIMARY KEY(song_ID, artist_ID),
    FOREIGN KEY (song_ID)
    REFERENCES Song(song_ID),
    FOREIGN KEY(artist_ID)
    REFERENCES Artist(artist_ID)
    );
    """
    create_table_Feature = """
    CREATE TABLE IF NOT EXISTS Feature(
    song_ID INTEGER PRIMARY KEY,
    FOREIGN KEY(song_ID)
    REFERENCES Song(song_ID)
    );
    """
    create_table_featured = """
    CREATE TABLE IF NOT EXISTS featured(
    song_ID INTEGER ,
    artist_ID INTEGER ,
    PRIMARY KEY(song_ID, artist_ID),
    FOREIGN KEY (song_ID)
    REFERENCES Feature(song_ID),
    FOREIGN KEY(artist_ID)
    REFERENCES Artist(artist_ID)
    );
    """
    create_table_genreSong = """
    CREATE TABLE IF NOT EXISTS genre_song (
    song_ID INTEGER ,
    genre_ID INTEGER ,
    PRIMARY KEY(song_ID, genre_ID),
    FOREIGN KEY (song_ID)
    REFERENCES Song(song_ID),
    FOREIGN KEY(genre_ID)
    REFERENCES Genre(genre_ID)
    );
    """
    create_table_haveA = """
    CREATE TABLE IF NOT EXISTS Have_A(
        album_ID INTEGER,
        feedback_ID INTEGER,
        PRIMARY KEY (feedback_ID),
        FOREIGN KEY(album_ID)
            REFERENCES Album(album_ID),
        FOREIGN KEY (feedback_ID)
            REFERENCES Feedback(feedback_ID)
    );
    """
    create_table_haveS = """
    CREATE TABLE IF NOT EXISTS Have_s(
    song_ID INTEGER,
    feedback_ID INTEGER,
    PRIMARY KEY(feedback_ID),
    FOREIGN KEY(song_ID)
    REFERENCES Song(song_ID),
    FOREIGN KEY(feedback_ID)
    REFERENCES Feedback(feedback_ID)
    );
    """
    create_table_produce = """
    CREATE TABLE IF NOT EXISTS Produce(
    artist_ID INTEGER,
    album_ID INTEGER PRIMARY KEY,
    FOREIGN KEY(album_ID)
    REFERENCES Album(album_ID),
    FOREIGN KEY(artist_ID)
    REFERENCES Artist(artist_ID)
    );
    """
    create_table_embrace = """
    CREATE TABLE IF NOT EXISTS embrace(
    genre_ID INTEGER,
    album_ID INTEGER,
    PRIMARY KEY(genre_ID , album_ID),
    FOREIGN KEY(genre_ID)
    REFERENCES Genre(genre_ID),
    FOREIGN KEY(album_ID)
    REFERENCES Album(album_ID)
    );
    """
    create_table_contain = """
    CREATE TABLE IF NOT EXISTS contain
    (
        song_ID INTEGER,
        album_ID INTEGER,
        PRIMARY KEY(song_ID),
        FOREIGN KEY(song_ID)
            REFERENCES Song(song_ID),
        FOREIGN KEY(album_ID)
            REFERENCES Album(album_ID)
    );
    """
    create_table_focusesOn = """
    CREATE TABLE IF NOT EXISTS Focuses_On
    (
        artist_ID INTEGER,
        genre_ID INTEGER,
        PRIMARY KEY(artist_ID, genre_ID),
        FOREIGN KEY(artist_ID)
            REFERENCES Artist(artist_ID),
        FOREIGN KEY(genre_ID)
            REFERENCES Genre(genre_ID)
    );
    """

    #ACTUALLY CREATE THE TABLES
    execute_query(my_connect, create_song_table)
    execute_query(my_connect, create_table_genre)
    execute_query(my_connect, create_album_table)
    execute_query(my_connect, create_table_artist)
    execute_query(my_connect, create_artistBand_table) 
    execute_query(my_connect, create_artistSinger_table)
    execute_query(my_connect, create_feedback_table)
    execute_query(my_connect, create_rating_table)
    execute_query(my_connect, create_table_contain)
    execute_query(my_connect, create_table_created)
    execute_query(my_connect, create_table_embrace)
    execute_query(my_connect, create_table_Feature)
    execute_query(my_connect, create_table_featured)
    execute_query(my_connect, create_table_produce)
    execute_query(my_connect, create_table_focusesOn)
    execute_query(my_connect, create_table_haveS)
    execute_query(my_connect, create_table_genreSong)
    execute_query(my_connect, create_table_haveA)
#Insert into tables
#First, entity tables

#Song table
    with open("songs.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["title"]
            releaseYear = row["release year"]
            length = row["length"]
            my_connect.execute("INSERT INTO Song(title, releaseYear, song_length) VALUES(?, ?, ?)", (title, releaseYear, length))
            my_connect.commit()

#Genre Table
    with open("genre.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            my_connect.execute("INSERT INTO Genre(genre_name) VALUES(?)", [name])
            my_connect.commit()
    
#ARTIST TABLE
    with open("artist.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            my_connect.execute("INSERT INTO Artist(artist_Name) VALUES(?)", (name,))
            my_connect.commit()

#Artist_Singer Table
    with open("artist_singer.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            year = row["birthyear"]
            my_connect.execute("INSERT INTO Artist_Singer(birthYear) VALUES (?)", (year,))
            my_connect.execute("""
            INSERT or IGNORE INTO Artist_Singer(artist_ID) 
            SELECT artist_ID FROM Artist WHERE artist_Name = (?)""", [name])
            my_connect.commit()

    #Artist_Band Table
    with open("band.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            year = row["formationyear"]
            my_connect.execute("INSERT INTO Artist_Band(formationYear) VALUES (?)", (year,))
            my_connect.execute(
                """INSERT or IGNORE INTO Artist_Band(artist_ID) 
                SELECT artist_ID FROM Artist WHERE artist_Name = (?)""", [name])
            my_connect.commit()
    
    #Album Table
    with open("album.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["title"]
            num = row["no of tracks"]
            year = row["release year"]
            my_connect.execute("INSERT INTO Album(title, release_year, numTracks) VALUES(?,?, ?)", [title, year, num])
            my_connect.commit()

    #Feedback Table
    #Actually Rating Table
    with open("rating.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            num = int(row["stars"])
            my_connect.execute("INSERT INTO Rating(stars) VALUES( ?)", [num])
            my_connect.commit()
            
    # Have_S Table <feedback to rating>
    with open("rating-song.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["song"]
            rate = int(row["rating"])
            my_connect.execute("""
            INSERT INTO Have_S(song_ID, feedback_ID) SELECT Song.song_ID, Rating.feedback_ID FROM Song, Rating
            WHERE Song.title = (?) AND Rating.stars = (?)
            """, [title, rate])
            my_connect.commit()
    ##Populate later

#NOW THE RELATIONSHIP TABLES

    #genre_song table
    with open("gs.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["title"]
            for name in row["name"].split(", "):
                my_connect.execute("""
                INSERT INTO genre_song(song_ID, genre_ID) SELECT Song.song_ID, Genre.genre_ID FROM Song, Genre
                WHERE Song.title = (?) AND Genre.genre_name = (?)
                """, [title, name]) 
            my_connect.commit()

    #'created' table <song to artist>
    with open("Song and Artists.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["song"]
            name = row["artist"]
            my_connect.execute("""
            INSERT INTO created(song_ID, artist_ID) SELECT Song.song_ID, Artist.artist_ID FROM Artist, Song
            WHERE Song.title = (?) AND Artist.artist_Name = (?)
                """, [title, name])
            my_connect.commit()
    
    #'produce' table <artist to album>
    with open("Album Artist.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["album"]
            name = row["artist"]
            my_connect.execute("""
            INSERT or IGNORE INTO produce(artist_ID, album_ID) SELECT Artist.artist_ID, Album.album_ID FROM Artist, Album
            WHERE Artist.artist_Name = (?) AND Album.title = (?)
                """, [name, title])
            my_connect.commit()
    
    #'contain' table <album to song>
    with open("Song Album.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["song"]
            name = row["album"]
            my_connect.execute("""
            INSERT or IGNORE INTO contain(song_ID, album_ID) SELECT Song.song_ID, Album.album_ID FROM Song, Album
            WHERE Song.title = (?) AND Album.title = (?)
                """, [title, name])
            my_connect.commit()
    

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


#for other SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


#def insert_query_relationship(connection, file, query, ID):
#    jjj


main()
