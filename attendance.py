
from db import db
from sqlalchemy import text
from datetime import datetime
from datetime import timedelta


def check_in(user_id, tyoaika, tuntilaji):
    if user_id is not None:
        query = text("INSERT INTO Attendance (user_id, check_in, working_time, Hour_class) VALUES (:user_id, :check_in, :tyoaika, :tuntilaji)")
        db.session.execute(query, {"user_id": user_id, "check_in": datetime.now(), "tyoaika": tyoaika, "tuntilaji": tuntilaji})
        db.session.commit()

def check_out(user_id, checkout_reason):
    if user_id is not None:
        latest_attendance = get_latest_attendance(user_id)
        if latest_attendance:
            query = text("UPDATE Attendance SET check_out = :check_out, checkout_reason = :checkout_reason WHERE id = :attendance_id")
            db.session.execute(query, {"check_out": datetime.now(), "checkout_reason": checkout_reason, "attendance_id": latest_attendance.id})
            db.session.commit()




def get_user_attendance_history(user_id):
    user_attendance = get_user_attendance(user_id)

    attendance_history = []

    for record in user_attendance:
        check_in_time = record.check_in
        check_out_time = record.check_out

        if check_out_time:
            work_duration = check_out_time - check_in_time
        else:
            work_duration = timedelta(0) 

        attendance_history.append({
            'date': check_in_time.strftime('%Y-%m-%d'),
            'day_of_week': check_in_time.strftime('%A'),
            'work_duration': work_duration
        })

    return attendance_history


def get_latest_attendance(user_id):
    query = text("SELECT * FROM Attendance WHERE user_id = :user_id ORDER BY check_in DESC LIMIT 1")
    result = db.session.execute(query, {"user_id": user_id}).fetchone()
    return result


def get_user_attendance(user_id):
    query = text("SELECT * FROM Attendance WHERE user_id = :user_id")
    result = db.session.execute(query, {"user_id": user_id}).fetchall()
    return result

def get_user_id(username):
    query = text("SELECT id FROM Users WHERE username = :username")
    result = db.session.execute(query, {"username": username}).fetchone()
    if result:
        return result.id
    else:
        return None
    


