from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.analyzer.lexicon.update({
            'moon': 4,   # Ajout de termes crypto-spécifiques
            'rekt': -4
        })
    
    def analyze(self, text: str) -> float:
        return self.analyzer.polarity_scores(text)['compound']
    
    def bulk_analyze(self, texts: list) -> dict:
        scores = [self.analyze(text) for text in texts]
        return {
            "mean": np.mean(scores),
            "std": np.std(scores),
            "count": len(scores)
        }