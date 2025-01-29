import os
from datetime import datetime
from utils.logger import setup_logger
from data.twitter_scraper import TwitterScraper
from analysis.sentiment_analyzer import SentimentAnalyzer
from alerts.telegram_notifier import TelegramNotifier

logger = setup_logger("Main")

def main():
    # Configuration initiale
    scraper = TwitterScraper()
    analyzer = SentimentAnalyzer()
    notifier = TelegramNotifier()
    
    # Liste des cryptos à surveiller
    target_cryptos = ["RUNE", "ATOM", "DOT"]
    
    try:
        for crypto in target_cryptos:
            # Collecte des données
            tweets = scraper.get_recent_tweets(crypto)
            logger.info(f"Collected {len(tweets)} tweets for {crypto}")
            
            # Analyse de sentiment
            scores = [analyzer.analyze(tweet) for tweet in tweets]
            avg_score = sum(scores) / len(scores) if scores else 0
            
            # Décision et notification
            if avg_score > 0.7:  # Seuil personnalisable
                message = f"🚀 Opportunité sur {crypto} !\nScore: {avg_score:.2f}"
                notifier.send_alert(message)
                
    except Exception as e:
        logger.error(f"Erreur critique: {str(e)}")

if __name__ == "__main__":
    main()