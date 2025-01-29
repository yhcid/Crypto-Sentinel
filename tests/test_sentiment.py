import pytest
from src.analysis.sentiment_analyzer import SentimentAnalyzer

def test_positive_sentiment():
    analyzer = SentimentAnalyzer()
    assert analyzer.analyze("RUNE is going to the moon!") > 0.5

def test_negative_sentiment():
    analyzer = SentimentAnalyzer()
    assert analyzer.analyze("I just got rekt on ATOM") < -0.3