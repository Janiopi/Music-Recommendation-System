import re

class PromptProcessing():
    @staticmethod
    def tokenize(prompt: str) -> list[str]:
        prompt_min = prompt.lower()
        prompt_clean = re.sub(r'[^\w\s]',"",prompt_min)
        tokens = prompt_clean.split()
        return tokens

    @staticmethod
    def get_feature_vector(tokens: list[str], dict_key_words: dict[str,dict[str,float]]) -> dict[str,float]:
        feature_vector = { "vibe":0.5, "energy":0.5,"melancholy":0.5,"acoustic":0.5,"instrumental":0.5,"darkness":0.5}
        for token in tokens:
            if token in dict_key_words:
                features = dict_key_words[token]
                for dict_feat,dict_score in features.items():
                    if dict_feat in feature_vector:
                        feature_vector[dict_feat] += dict_score
        result = []
        for value in feature_vector.values():
            result.append(value)
        return result


