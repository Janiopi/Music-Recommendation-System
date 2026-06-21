from prompt_processing import PromptProcessing
import json


p = PromptProcessing()

try:
    with open("diccionario_intenciones.json","r") as f:
        dictionary_intentions = json.load(f)
except FileNotFoundError:
        print("The file could not be found.")
except json.JSONDecodeError:
        print("Invalid JSON structure detected.")


prompt = "Quiero una canción oscuro con ambiente cyberpunk!!!"

tokens = p.tokenize(prompt)
print(tokens)
feat_vectors = p.get_feature_vector(tokens,dictionary_intentions)

print(feat_vectors)