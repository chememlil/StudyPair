from flask import Blueprint, request, jsonify
from app.models import Student
from app import db

student = Blueprint('student', __name__)

@student.route('/', methods=['POST'])
def get_students():
    students = Student.query.all()
    student_list = [{"id": student.id, "name": student.name} for student in students]
    return jsonify(student_list), 200

@student.route('/', methods=['POST'])
def add_student():
    data = request.json
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name is required"}), 400

    student = Student(name=name)
    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student added successfully"}), 201

@student.route('/<int:id>', methods=['DELETE'])
def delete_student(id):
    # Use `db.session.get()` to fetch the student
    student = db.session.get(Student, id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"}), 200
