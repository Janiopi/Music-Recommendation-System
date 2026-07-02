from models.song import Song,SongRepository
import math

class Recommender:
    def __init__(self,repo: SongRepository ):
        self.repo = repo

    def recommend_song(self, target_vector: list[float], top_n: int = 5) -> list[dict]:
        songs = self.repo.get_all()
        songs_score = []
        for song in songs: 
            songs_score.append({"Song": song, "score":cosine_similarity(song.getFeatureVector(),target_vector)}) 

        sorted_songs = sorted(songs_score, key=lambda x: x["score"], reverse=True)       

        # Return just the top n
        return sorted_songs[:top_n]

def dot_product(vector1: list[float],vector2: list[float]) -> float:
    
    if(len(vector1) != len(vector2)):
        raise ValueError("Vectors should be of the same size!")
    n = len(vector1)

    dot_prod = 0
    for i in range(0,n):
        dot_prod = vector1[i]*vector2[i] + dot_prod

    return dot_prod

def vector_norm(vector: list[float]) -> float:
    norm = 0
    for i in vector:
        norm = i*i + norm
    
    return math.sqrt(norm)

def cosine_similarity(vector1: list[float], vector2: list[float]) -> float:
    num = dot_prod(vector1,vector2)
    den = vector_norm(vector1)*vector_norm(vector2)
    if (den == 0):
        return 0.0
    return num/den

obj_vector = [1,2,3,4,5,6]
cancion = Song("Get Lucky","Daft Punk","Pop/Funk","RAM","2014",1,1,0,0,3,0)
cancion_vector = cancion.getFeatureVector()

dot_prod = dot_product(obj_vector,cancion_vector)
print(dot_prod)