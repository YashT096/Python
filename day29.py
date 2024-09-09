#Today we are going to learn about Handling APIs
 

#Structure of an API
#GET        Used for object retrieval
#POST       Used for object creation and object actions
#PUT        Used for object update
#DELETE     Used for object deletion

# let's import the flask

from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection URI
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']  # accessing the database

# Route to get all students
@app.route('/api/v1.0/students', methods=['GET'])
def students():
    students_list = list(db.students.find())
    return Response(dumps(students_list), mimetype='application/json')

# Route to get a single student by id
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def single_student(id):
    student = db.students.find_one({'_id': ObjectId(id)})
    if student:
        return Response(dumps(student), mimetype='application/json')
    return Response(json.dumps({"error": "Student not found"}), mimetype='application/json', status=404)

# Route to create a student
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    name = request.form.get('name')
    country = request.form.get('country')
    city = request.form.get('city')
    skills = request.form.get('skills', '').split(', ')
    bio = request.form.get('bio')
    birthyear = request.form.get('birthyear')
    created_at = datetime.now()

    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at
    }

    db.students.insert_one(student)
    return Response(dumps({"result": "Student created successfully"}), mimetype='application/json', status=201)

# Route to update a student by id
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    query = {"_id": ObjectId(id)}
    name = request.form.get('name')
    country = request.form.get('country')
    city = request.form.get('city')
    skills = request.form.get('skills', '').split(', ')
    bio = request.form.get('bio')
    birthyear = request.form.get('birthyear')
    updated_at = datetime.now()

    updated_data = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'updated_at': updated_at
    }

    result = db.students.update_one(query, {'$set': updated_data})

    if result.matched_count:
        return Response(dumps({"result": "Student updated successfully"}), mimetype='application/json', status=200)
    return Response(json.dumps({"error": "Student not found"}), mimetype='application/json', status=404)

# Route to delete a student by id
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    result = db.students.delete_one({"_id": ObjectId(id)})

    if result.deleted_count:
        return Response(dumps({"result": "Student deleted successfully"}), mimetype='application/json', status=200)
    return Response(json.dumps({"error": "Student not found"}), mimetype='application/json', status=404)

# Running the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
