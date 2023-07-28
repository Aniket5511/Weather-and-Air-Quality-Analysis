import pymongo
import pandas as pd
from pymongo import MongoClient
client = MongoClient('mongodb+srv://aniket5511:aniket5511@cluster0.2pqbq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.weather
collection = db.weatherAPI
data = pd.DataFrame(list(collection.find()))

print(data.head())

