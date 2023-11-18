
from db import db
from sqlalchemy import text
from datetime import datetime

def check_in(user_id):
    if user_id is not None:
        query = text("INSERT INTO Attendance (user_id, check_in) VALUES (:user_id, :check_in)")
        db.session.execute(query, {"user_id": user_id, "check_in": datetime.now()})
        db.session.commit()

def check_out(user_id):
    if user_id is not None:
        latest_attendance = get_latest_attendance(user_id)
        if latest_attendance:
            query = text("UPDATE Attendance SET check_out = :check_out WHERE id = :attendance_id")
            db.session.execute(query, {"check_out": datetime.now(), "attendance_id": latest_attendance.id})
            db.session.commit()




def get_user_attendance_history(user_id):
    # Fetch the user's attendance records
    user_attendance = get_user_attendance(user_id)

    # Create a dictionary to store day-wise attendance
    daywise_attendance = {}

    for record in user_attendance:
        check_in_time = record.check_in
        check_out_time = record.check_out

        # Calculate the work duration for each record
        if check_out_time:
            work_duration = check_out_time - check_in_time
        else:
            work_duration = timedelta(0)  # Incomplete attendance, set to zero for now

        # Extract the day of the week
        day_of_week = check_in_time.strftime('%A')

        # Update the day-wise attendance dictionary
        if day_of_week not in daywise_attendance:
            daywise_attendance[day_of_week] = work_duration
        else:
            daywise_attendance[day_of_week] += work_duration

    return daywise_attendance





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
    


