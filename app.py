from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"
app.config["MONGO_URI"] = "mongodb://localhost:27107/user"
mongo = PyMongo(app)

@app.route('/test_db', methods=['GET'])
def test_db():
    try:
        mongo.db.info.find_one()
        return jsonify("Connected to MongoDB"), 200
    except Exception as e:
        return jsonify(str(e)), 500


@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _uid = _json['uid']
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']
    
    if _uid and _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        new_user = mongo.db['info'].insert_one({'uid':_uid, 'name': _name, 'email':_email, 'password':_password})

        response = jsonify("user added successfully")
        response.status_code = 200

        return response

@app.route('/get', methods=['GET'])
def get_users():
    users = mongo.db.info.find()
    # response = dumps(users)
    return users



if __name__ == "__main__":
    app.run(debug=True)
