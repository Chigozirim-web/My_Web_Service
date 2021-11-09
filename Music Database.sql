CREATE TABLE Song(
song_ID INT PRIMARY KEY,
title VARCHAR(20),
song_length INT,
releaseYear INT
);

CREATE TABLE Feedback(
feedback_ID INT,
comment VARCHAR(256),
PRIMARY KEY(feedback_ID)
);

CREATE TABLE Rating(
feedback_ID INT PRIMARY KEY,
stars INT,
FOREIGN KEY(feedback_ID)
REFERENCES Feedback(feedback_ID)
);

CREATE TABLE Album(
album_id INT PRIMARY KEY,
release_year INT,
numTracks INT,
title VARCHAR(128)
);

CREATE TABLE Genre(
genre_ID INT PRIMARY KEY,
genre_name VARCHAR(20)
);

CREATE TABLE Artist(
artist_ID INT PRIMARY KEY
artist_Name VARCHAR(20),
);

CREATE TABLE Artist_Band(
artist_ID INT PRIMARY KEY,
formationYear INT,
FOREIGN KEY(artist_ID)
REFERENCES Artist(artist_ID)
);

CREATE TABLE Artist_Singer(
artist_ID INT PRIMARY KEY,
birthYear INT,
FOREIGN KEY(artist_ID)
REFERENCES Artist(artist_ID)
);

CREATE TABLE created(
song_ID INT ,
artist_ID INT ,
PRIMARY KEY(song_ID, artist_ID),
FOREIGN KEY (song_ID)
REFERENCES Song(song_ID),
FOREIGN KEY(artist_ID)
REFERENCES Artist(artist_ID)
);

CREATE TABLE Feature(
song_ID INT PRIMARY KEY,
FOREIGN KEY(song_ID)
REFERENCES Song(song_ID)
);

CREATE TABLE featured(
song_ID INT ,
artist_ID INT ,
PRIMARY KEY(song_ID, artist_ID),
FOREIGN KEY (song_ID)
REFERENCES Feature(song_ID),
FOREIGN KEY(artist_ID)
REFERENCES Artist(artist_ID)
);

CREATE TABLE genre_song (
song_ID INT ,
genre_id INT ,
PRIMARY KEY(song_ID, genre_ID),
FOREIGN KEY (song_ID)
REFERENCES Song(song_ID),
FOREIGN KEY(genre_ID)
REFERENCES Genre(genre_ID)
);

CREATE TABLE Have_s(
song_ID INT,
feedback_ID INT,
PRIMARY KEY(feedback_ID),
FOREIGN KEY(song_id)
REFERENCES Song(song_ID),
FOREIGN KEY(feedback_ID)
REFERENCES Feedback(feedback_ID)
);

CREATE TABLE Produce(
artist_ID INT,
album_ID INT PRIMARY KEY,
FOREIGN KEY(album_ID)
REFERENCES Album(album_ID),
FOREIGN KEY(artist_ID)
REFERENCES Artist(artist_ID)
);

CREATE TABLE embrace(
genre_ID INT,
album_ID INT,
PRIMARY KEY(genre_ID , album_ID),
FOREIGN KEY(genre_ID)
REFERENCES Genre(genre_ID),
FOREIGN KEY(album_ID)
REFERENCES Album(album_ID)
);

CREATE TABLE contain
(
    song_id INT,
    album_id INT,
    PRIMARY KEY(song_id),
    FOREIGN KEY(song_id)
        REFERENCES Song(song_id),
    FOREIGN KEY(album_id)
        REFERENCES Album(album_id)
);

CREATE TABLE Focuses_On
(
    artist_id INT,
    genre_id INT,
    PRIMARY KEY(artist_id, genre_id),
    FOREIGN KEY(artist_id)
        REFERENCES Artist(artist_id),
    FOREIGN KEY(genre_id)
        REFERENCES Genre(genre_id)
);
