from flask import Flask, request, jsonify
from flask_cors import CORS
from config import create_app, db
from models import Camper, Activity, Signup

app = create_app()
CORS(app)

with app.app_context():
    db.create_all()

app.route('/campers', methods=['GET'])
def get_campers():
    campers = Camper.query.all()
    return jsonify([{"id": c.id, "name": c.name, "age": c.age} for c in campers])

@app.route('/campers', methods=['POST'])
def add_camper():
    data = request.jsom
    new_camper = Camper(name=data['name'], age=data['age'])
    db.session.add(new_camper)
    db.session.commit()
    return jsonify({"id": new_camper.id, "name": new_camper.name, "age": new_camper})

@app.route('/activities', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    return jsonify([{"id": a.id, "name": a.name, "difficulty": a.difficulty} for a in activities])

@app.route('/signup', methods=['POST'])
def signup_activity():
    data = request.json
    new_signup = Signup(time=data['time'], camper_id=data['camper_id'], activity_id=data['camper_id'])
    db.session.add(new_signup)
    db.session.commit()
    return jsonify({"id": new_signup.id})

@app.route('/activities', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get_or_404(id)
    db.session.delete(activity)
    db.session.commit()
    return jsonify({"message": "Activity deleted"}), 204


if __name__ == '__main__':
    app.run(port=5555, debug=True)