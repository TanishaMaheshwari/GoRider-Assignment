import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId
from flask import abort

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://mongo:27017/mydb')  

mongodb = PyMongo(app).db

@app.route("/api/post_user", methods=['POST'])
def post_user():
        data = request.json
        
        required_fields = ['uid', 'name', 'email', 'password']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"{field} is required"}), 400

        user = {
            'uid': data['uid'],
            'name': data['name'],
            'email': data['email'],
            'password': data['password'],
            'isComplete': False
        }
        
        try:
            mongodb.user_info.insert_one(user)
            return jsonify({"msg": "User added successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route("/api/get_user", methods=['GET'])
def get_user():
    try:
        user_info = mongodb.user_info.find()
        users = []

        for user in user_info:
            user_data = {
                "id": str(user['_id']),
                "uid": user['uid'],
                "name": user['name'],
                "email": user['email'],
                "password": user['password'],
                "isComplete": user['isComplete']
            }
            users.append(user_data)

        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/put_user/<string:id>", methods=['PUT'])
def put_user(id):
    mongoid = ObjectId(id)
    updated_data = request.json
        
    try:
            result = mongodb.user_info.find_one_and_update(
                {"_id": mongoid},
                {"$set": updated_data},
                return_document=True
            )
            if result:
                return jsonify({"msg": "User updated successfully."}), 200
            else:
                return jsonify({"error": "User not found."}), 404
    except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route("/api/delete_user/<string:id>", methods=['DELETE'])
def delete_user(id):
        mongoid = ObjectId(id)
        try:
            result = mongodb.user_info.find_one_and_delete({"_id": mongoid})
            if result:
                return jsonify({"msg": "User deleted successfully."}), 200
            else:
                return jsonify({"error": "User not found."}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
