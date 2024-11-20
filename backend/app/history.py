from flask import Blueprint, jsonify
from app.models import PairingHistory, Student
from app import db

history = Blueprint('history', __name__)

@history.route('/history/', methods=['GET'])
def get_history():
    # Fetch all pairing history from the database
    all_history = PairingHistory.query.all()
    history_data = []
    
    for pair in all_history:
        student1 = Student.query.get(pair.student1_id)
        student2 = Student.query.get(pair.student2_id)
        history_data.append({
            'student1_name': student1.name,
            'student2_name': student2.name,
            'week': pair.week
        })
    
    return jsonify(history_data)