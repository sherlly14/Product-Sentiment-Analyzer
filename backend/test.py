from pymongo import MongoClient
import certifi

uri = "mongodb+srv://sibilannat30:Sibil382@cluster0.pmhuizc.mongodb.net/Majorproject1?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(
        uri,
        tls=True,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=10000
    )

    client.admin.command("ping")
    print("✅ Connected successfully!")

except Exception as e:
    print("❌ Connection failed")
    print(e)