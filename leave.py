from sqlalchemy import text
from db import db



def create_leave_request(user_id, start_date, end_date, reason):
    if user_id is not None:
        query = text("INSERT INTO Leave_requests (user_id, start_date, end_date, reason, status) "
                     "VALUES (:user_id, :start_date, :end_date, :reason, 'Pending')")
        db.session.execute(
            query,
            {
                "user_id": user_id,
                "start_date": start_date,
                "end_date": end_date,
                "reason": reason,
            },
        )
        db.session.commit()
