from pymongo import MongoClient
import pandas as pd
import certifi

uri = "mongodb+srv://sibilannat30:Sibil382@cluster0.pmhuizc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, tlsCAFile=certifi.where())

print("✅ Connected to MongoDB Atlas!")

db = client["Majorproject1"]      # <-- Capital M
collection = db["reviews"]

df = pd.read_csv("data/reviews_with_sentiment.csv")

collection.delete_many({})        # Optional: clears old data

collection.insert_many(df.to_dict("records"))

print(f"✅ Inserted {len(df)} reviews into MongoDB!")