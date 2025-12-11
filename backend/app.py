from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = "mongodb+srv://Harshit_Rohtela:9kKJADYjv64P1H34@cluster0.hi1rg.mongodb.net/"

client = MongoClient(MONGO_URI)

db = client.test

collection = db["Assignment"]

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get("name")
        description = request.form.get("description")
        
        collection.insert_one({"name": name, "description": description})
        
        return jsonify({"message" : "Data submitted successfully"}), 200
    
    except Exception as e:
        
        return jsonify({"error" : str(e)}), 400
    
    
@app.route('/view', methods=['GET'])
def view():
    
    data = list(collection.find())
    
    for record in data:
        record["_id"] = str(record["_id"])
    
    return jsonify({"data": data})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)
        
