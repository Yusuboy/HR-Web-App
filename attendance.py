
from db import db
from sqlalchemy import text
from datetime import datetime

def check_in(username):
    print(username)
    user_id = username
    if user_id is not None:
        query = text("INSERT INTO Attendance (user_id, check_in) VALUES (:user_id, :check_in)")
        db.session.execute(query, {"user_id": user_id, "check_in": datetime.utcnow()})
        db.session.commit()

def check_out(username):
    print(username)
    user_id = get_user_id(username)
    if user_id is not None:
        latest_attendance = get_latest_attendance(user_id)
        if latest_attendance:
            query = text("UPDATE Attendance SET check_out = :check_out WHERE id = :attendance_id")
            db.session.execute(query, {"check_out_time": datetime.utcnow(), "attendance_id": latest_attendance.id})
            db.session.commit()

def get_latest_attendance(user_id):
    query = text("SELECT * FROM Attendance WHERE user_id = :user_id ORDER BY check_in_time DESC LIMIT 1")
    result = db.session.execute(query, {"user_id": user_id}).fetchone()
    return result

def get_user_id(username):
    query = text("SELECT id FROM Users WHERE username = :username")
    result = db.session.execute(query, {"username": username}).fetchone()
    if result:
        return result.id
    else:
        return None