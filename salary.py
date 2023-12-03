# In salary.py

from db import db
from sqlalchemy import text
from datetime import datetime

def calculate_total_earnings(start_date, end_date, hourly_rate):
    work_duration_hours = calculate_work_duration_in_hours(start_date, end_date)
    total_earnings = work_duration_hours * hourly_rate
    return total_earnings

def calculate_work_duration_in_hours(start_date, end_date):
    # print(start_date)
    # print(end_date)
    print(start_date)
    print(end_date)
   
 
    work_duration = datetime.combine(datetime.today(), end_date) - datetime.combine(datetime.today(), start_date)

    print(work_duration)
    work_duration_hours = work_duration.total_seconds() / 60
    print(work_duration_hours)
    return work_duration_hours

def update_salary_record(user_id, start_date, end_date, hourly_rate, total_earnings):
    query = """
    INSERT INTO Salaries (user_id, start_date, end_date, hourly_rate, total_earnings)
    VALUES (:user_id, :start_date, :end_date, :hourly_rate, :total_earnings)
    ON CONFLICT (user_id, end_date) DO UPDATE
    SET hourly_rate = EXCLUDED.hourly_rate, total_earnings = EXCLUDED.total_earnings
"""

    db.session.execute(
        text(query),
        {
            "user_id": user_id,
            "start_date": start_date,
            "end_date": end_date,
            "hourly_rate": hourly_rate,
            "total_earnings": total_earnings,
        },
    )


    db.session.commit()


