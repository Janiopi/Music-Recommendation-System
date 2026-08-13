from prompt_processing import PromptProcessing
from recommender_engine import Recommender
from SQLiteSongRepository import SQLiteSongRepository
from models.song import SongRepository,Song
import json

def seed_database(repo: SongRepository):
    songs_to_seed = [
        # Glimpse of Us - Joji (Triste / Lluvioso)
        Song("Glimpse of Us", "Joji", "Pop/R&B", "SMITHEREENS", "2022-06-10", 
             0.2, 0.2, 0.95, 0.85, 0.1, 0.6),
        
        # Blinding Lights - The Weeknd (Fiesta / Bailable)
        Song("Blinding Lights", "The Weeknd", "Synthwave", "After Hours", "2019-11-29", 
             0.8, 0.9, 0.2, 0.0, 0.1, 0.5),
        
        # Harlem Nocturne - The Viscounts (Neo-Noir / Oscuro)
        Song("Harlem Nocturne", "The Viscounts", "Jazz", "Harlem Nocturne", "1959-01-01", 
             0.3, 0.3, 0.6, 0.6, 0.95, 0.9),
             
        # Lofi Study Beat - Lofi Girl (Estudiar / Instrumental)
        Song("Lofi Study Beat", "Lofi Girl", "Lofi", "Study Beats", "2020-01-01", 
             0.5, 0.2, 0.4, 0.4, 0.95, 0.2),

        # Don't Stop Me Now - Queen (Alegre / Alta Energía)
        Song("Don't Stop Me Now", "Queen", "Rock", "Jazz", "1978-11-10", 
             0.85, 0.95, 0.05, 0.2, 0.05, 0.0)
    ]

    print("Insertando catálogo de prueba en la base de datos...")
    for song in songs_to_seed:
        repo.create(song)
    print("Base de datos poblada con éxito!")

try:
    with open("dictionary_key_words.json","r") as f:
        dictionary_intentions = json.load(f)
except FileNotFoundError:
        print("The file could not be found.")
except json.JSONDecodeError:
        print("Invalid JSON structure detected.")

if __name__ == "__main__":
        # Instances
        repo = SQLiteSongRepository("songs.db")
        # Seeding
        if not repo.get_all():
                print("Poblando base de datos...")
                seed_database(repo)
        # Processing user prompt
        recommender = Recommender(repo)
        user_prompt = input("¿Qué tipo de música quieres escuchar?: ")
        p = PromptProcessing()
        tokens = p.tokenize(user_prompt)
        print(tokens)
        target_vector = p.get_feature_vector(tokens,dictionary_intentions)
        print(f"Target vector: {target_vector}")
        print("TIPO DEL TARGET VECTOR:", type(target_vector))

        # Finding recommendations  
        recommendantions = recommender.recommend_song(target_vector,5)
        print(recommendantions)


