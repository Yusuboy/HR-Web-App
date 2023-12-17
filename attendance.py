from datetime import datetime, timedelta
from sqlalchemy import text
from db import db
from salary import calculate_total_earnings, update_salary_record

def check_in(user_id, tyoaika, tuntilaji):
    if user_id is not None:
        query = text(
            "INSERT INTO Attendance (user_id, check_in, working_time, Hour_class) "
            "VALUES (:user_id, :check_in, :tyoaika, :tuntilaji)"
        )
        db.session.execute(
            query,
            {
                "user_id": user_id,
                "check_in": datetime.now(),
                "tyoaika": tyoaika,
                "tuntilaji": tuntilaji,
            },
        )
        db.session.commit()

def check_out(user_id, checkout_reason):
    if user_id is not None:
        latest_attendance = get_latest_attendance(user_id)
        if latest_attendance:
            query = text(
                "UPDATE Attendance SET check_out = :check_out, "
                "checkout_reason = :checkout_reason "
                "WHERE id = :attendance_id"
            )
            db.session.execute(
                query,
                {
                    "check_out": datetime.now(),
                    "checkout_reason": checkout_reason,
                    "attendance_id": latest_attendance.id,
                },
            )
            db.session.commit()


            start_date = latest_attendance.check_in.date()
            start_time = latest_attendance.check_in.time()
            end_date = (
                latest_attendance.check_out.date()
                if latest_attendance.check_out
                else datetime.now().date()
            )

            end_time = (
                latest_attendance.check_out.time()
                if latest_attendance.check_out
                else datetime.now().time()
            )

            hourly_rate = 12.00

            total_earnings = calculate_total_earnings(start_time, end_time, hourly_rate)
            update_salary_record(user_id, start_date, end_date, hourly_rate, total_earnings)



def calculate_salary_for_attendance(user_id, start_date, end_date):
    total_earnings = calculate_total_earnings(user_id, start_date, end_date)
    return total_earnings


def get_user_attendance_history(user_id):
    query = text(
        "SELECT a.id AS attendance_id, u.id AS user_id, a.check_in, a.check_out, "
        "CASE WHEN a.check_out IS NOT NULL THEN a.check_out - a.check_in ELSE interval '0' END AS work_duration, "
        "to_char(a.check_in, 'YYYY-MM-DD') AS date, "
        "to_char(a.check_in, 'HH24:MI') AS check_in_time, "
        "to_char(a.check_out, 'HH24:MI') AS check_out_time, "
        "to_char(a.check_in, 'Day') AS day_of_week, "
        "s.hourly_rate, s.total_earnings "
        "FROM Attendance a "
        "JOIN Users u ON a.user_id = u.id "
        "LEFT JOIN Salaries s ON a.user_id = s.user_id AND a.check_in::date BETWEEN s.start_date AND COALESCE(s.end_date, CURRENT_DATE) "
        "WHERE u.id = :user_id "
        "ORDER BY a.check_in DESC;"
    )
    
    result = db.session.execute(query, {"user_id": user_id}).fetchall()

    return result


def get_latest_attendance(user_id):
    query = text(
        "SELECT id, user_id, working_time, hour_class, check_in, check_out, checkout_reason "
        "FROM Attendance WHERE user_id = :user_id ORDER BY check_in DESC LIMIT 1"
    )
    result = db.session.execute(query, {"user_id": user_id}).fetchone()
    return result


# def get_user_attendance(user_id):
#     query = text(
#         "SELECT a.id, a.user_id, a.working_time, a.hour_class, a.check_in, a.check_out, a.checkout_reason, "
#         "s.hourly_rate, s.total_earnings "
#         "FROM Attendance a "
#         "LEFT JOIN Salaries s ON a.user_id = s.user_id AND a.check_in::date BETWEEN s.start_date AND COALESCE(s.end_date, CURRENT_DATE) "
#         "WHERE a.user_id = :user_id "
#         "ORDER BY a.check_in DESC"
#     )
#     result = db.session.execute(query, {"user_id": user_id}).fetchall()
#     return result

def get_user_id(username):
    query = text("SELECT id FROM Users WHERE username = :username")
    result = db.session.execute(query, {"username": username}).fetchone()
    if result:
        return result.id




def get_all_users_work_history():
    query = text(
        "SELECT u.username, a.check_in, a.check_out, a.checkout_reason, "
        "s.hourly_rate, s.total_earnings "
        "FROM Users u "
        "LEFT JOIN Attendance a ON u.id = a.user_id "
        "LEFT JOIN Salaries s ON u.id = s.user_id AND "
        "a.check_in::date BETWEEN s.start_date AND COALESCE(s.end_date, CURRENT_DATE) "
        "ORDER BY u.username, a.check_in DESC"
    )

    result = db.session.execute(query).fetchall()
    return result
