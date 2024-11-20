from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

class Pair(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student1_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    student2_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    week = db.Column(db.Date, nullable=False)

class PairingHistory(db.Model):
    __tablename__ = 'pairing_history'

    id = db.Column(db.Integer, primary_key=True)
    student1_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    student2_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    week = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<PairingHistory student1={self.student1_id} student2={self.student2_id} week={self.week}>"