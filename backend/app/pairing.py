from flask import Blueprint, jsonify
from app.models import Student
import random

pairing = Blueprint('pairing', __name__)

@pairing.route('/', methods=['POST'])
def generate_pairs():
    # Fetch all students from the database
    students = Student.query.all()

    if not students:
        return jsonify({"error": "No students available to generate pairs"}), 400

    # Extract student names
    student_names = [student.name for student in students]

    # Shuffle and create pairs
    random.shuffle(student_names)
    pairs = [(student_names[i], student_names[i + 1]) for i in range(0, len(student_names) - 1, 2)]

    # Handle an odd number of students
    if len(student_names) % 2 != 0:
        pairs.append((student_names[-1], "No pair"))

    return jsonify({"message": "Pairs generated successfully", "pairs": pairs}), 200
