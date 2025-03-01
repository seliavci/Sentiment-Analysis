import praw
from textblob import TextBlob
import matplotlib.pyplot as plt

# Reddit API Bağlantısı
reddit = praw.Reddit(client_id="FVsbC7LzV45WM3NjkhBtYA",
                     client_secret="nCikirJKzmcMKtXVLbPgIyHzZOS5IQ",
                     user_agent="Admirable-Movie-2148")

# Gönderileri çekme
data = []
for submission in reddit.subreddit('all').search("oscars 2025", limit=1500):
    full_text = submission.title + " " + submission.selftext  # Title + Body
    if full_text.strip():  # Boş olanları alma
        data.append(full_text)

# Sentiment Analizi
sentiments = []
for text in data:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # [-1,1] aralığında değer döner
    sentiments.append(sentiment)

# Histogram Çizme
plt.figure(figsize=(8, 5))
plt.hist(sentiments, bins=30, color='blue', alpha=0.7)
plt.title('Sentiment Analysis Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
