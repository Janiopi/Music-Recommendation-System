from abc import ABC, abstractmethod
from typing import Optional

class Song():
    def __str__(self):
        return f"{self.title}-{self.artist}"
    def __repr__(self):
        return f"{self.title}-{self.artist}"
    def __init__(self, title: str, artist: str, genre: str, album: str, date: str,
                 vibe: float, energy: float, melancholy: float, 
                 acoustic: float, instrumental: float, darkness: float, 
                 id: Optional[int] = None):
        
        self.id = id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.album = album
        self.date = date
        
        # Feature vector ( 0.0 to 1.0 )
        self.vibe = vibe
        self.energy = energy
        self.melancholy = melancholy
        self.acoustic = acoustic
        self.instrumental = instrumental
        self.darkness = darkness
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getArtist(self):
        return self.artist
    
    def getGenre(self):
        return self.genre
    
    def getAlbum(self):
        return self.album
    
    def getDate(self):
        return self.date

    def getVibe(self):
        return self.vibe
    
    def getEnergy(self):
        return self.energy
    
    def getMelancholy(self):
        return self.melancholy
    
    def getAcoustic(self):
        return self.acoustic
    
    def getInstrumental(self):
        return self.instrumental
    
    def getDarkness(self):
        return self.darkness
  
    def getFeatureVector(self) -> list[float]:
        feature_vector = [self.vibe,self.energy,self.melancholy,self.acoustic,self.instrumental,self.darkness]
        return feature_vector

class SongRepository(ABC):

    @abstractmethod
    def create(self, song: Song) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Song]:
        pass
    
    @abstractmethod
    def get_all(self) -> list[Song]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def update(self, song: Song) -> None:
        pass