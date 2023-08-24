import pymongo
import certifi


me = {
    "name": "Ricky",
    "last_name": "Array",
    "age": 34,
    "hobbies": [],
    "address": {
        "street": "Schirra St",
        "city": "San Diego",
        "zip": 92154
    }
}


# database configuration
con_str = "mongodb+srv://FSDI:madre143@cluster0.9hzdatb.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("organika")