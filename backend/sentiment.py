import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv("data/reviews.csv")


def analyze_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Add sentiment column
df["sentiment"] = df["review_text"].apply(analyze_sentiment)

print(df.head())

# Save updated dataset
df.to_csv("data/reviews_with_sentiment.csv", index=False)

print("Sentiment analysis completed!")