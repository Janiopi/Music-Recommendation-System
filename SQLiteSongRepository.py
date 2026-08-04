import sqlite3
from models.song import Song, SongRepository

class SQLiteSongRepository(SongRepository): 
    
    def __init__(self, db_path: str):
        self.con = sqlite3.connect(db_path)
        cur = self.con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS songs(
        song_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(50) NOT NULL, 
        artist VARCHAR(50) NOT NULL,
        genre VARCHAR(50) NOT NULL,
        album VARCHAR(50) NOT NULL,
        release_date DATE,
        vibe FLOAT NOT NULL,
        energy FLOAT NOT NULL,
        melancholy FLOAT NOT NULL,
        acoustic FLOAT NOT NULL,
        instrumental FLOAT NOT NULL,
        darkness FLOAT NOT NULL
)""")
        self.con.commit()
    
    def find_by_id(self, id: int) -> Song:
        cur = self.con.cursor()
        cur.execute("SELECT * FROM songs WHERE song_id = :id",{"id": id})
        row = cur.fetchone()
        if row:
            return Song(
                id=row[0],
                title=row[1],
                artist=row[2],
                genre=row[3],
                album=row[4],
                date=row[5],
                vibe=float(row[6]),
                energy=float(row[7]),
                melancholy=float(row[8]),
                acoustic=float(row[9]),
                instrumental=float(row[10]),
                darkness=float(row[11])
            )
        return None
    
    def get_all(self) -> list[Song]:
        cur = self.con.cursor()
        cur.execute("SELECT * FROM songs")
        rows = cur.fetchall()
        if rows:
            songs = []
            for row in rows:
                songs.append(Song(id=row[0],title=row[1],artist=row[2],genre=row[3],album=row[4],date=row[5],vibe=float(row[6]),energy=float(row[7]),melancholy=float(row[8]),acoustic=float(row[9]),instrumental=float(row[10]),darkness=float(row[11])))
            return songs
        return []
    
    def delete(self, id: int) -> None:
        cur = self.con.cursor()
        cur.execute("DELETE FROM songs WHERE song_id = :id", {"id": id})
        self.con.commit()

    def update(self, song: Song) -> None:
        cur = self.con.cursor()
        cur.execute("""UPDATE songs SET 
            title = :title, artist = :artist, genre = :genre, album = :album,
            release_date = :release_date, vibe = :vibe, energy = :energy,
            melancholy = :melancholy, acoustic = :acoustic, instrumental = :instrumental,
            darkness = :darkness
            WHERE song_id = :id""", {
            "id": song.getId(),
            "title": song.getTitle(),
            "artist": song.getArtist(),
            "genre": song.getGenre(),
            "album": song.getAlbum(),
            "release_date": song.getReleaseDate(),
            "vibe": song.getVibe(),
            "energy": song.getEnergy(),
            "melancholy": song.getMelancholy(),
            "acoustic": song.getAcoustic(),
            "instrumental": song.getInstrumental(),
            "darkness": song.getDarkness()
        })
        self.con.commit()
        
    def create(self, song: Song) -> None:
        cur = self.con.cursor()
        cur.execute("""INSERT INTO songs 
            (title, artist, genre, album, release_date, vibe, energy, melancholy, acoustic, instrumental, darkness)
            VALUES (:title, :artist, :genre, :album, :release_date, :vibe, :energy, :melancholy, :acoustic, :instrumental, :darkness)""", {
            "title": song.getTitle(),
            "artist": song.getArtist(),
            "genre": song.getGenre(),
            "album": song.getAlbum(),
            "release_date": song.getDate(),
            "vibe": song.getVibe(),
            "energy": song.getEnergy(),
            "melancholy": song.getMelancholy(),
            "acoustic": song.getAcoustic(),
            "instrumental": song.getInstrumental(),
            "darkness": song.getDarkness()
        })
        self.con.commit()    