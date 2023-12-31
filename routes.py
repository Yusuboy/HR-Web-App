import secrets
from flask import (
 render_template, request,
 redirect,
 url_for, session, abort)

from app import app
from user import login, new_user
from attendance import (
    check_in,
    check_out,
    get_user_id,
    get_user_attendance_history,
    get_latest_attendance,
    get_all_users_work_history
)
from leave import (
    create_leave_request,
    get_user_leave_requests,
    get_all_leave_requests,
    update_leave_status
)

@app.route('/', methods=['GET', 'POST'])
def index():
    notification = None

    if request.method == 'POST':
        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'Admin' and password == '123456':
            # Set a session variable to identify the user as an admin
            session['is_admin'] = True
            session['csrf_token'] = secrets.token_hex(16)
            return redirect(url_for('admin_dashboard'))

        notification = login(username, password)

        if "successful" in notification:
            return redirect(url_for('user_home'))

    session['csrf_token'] = secrets.token_hex(16)
    return render_template('index.html', title='HR-Web-APP',
                           notification=notification,
                           csrf_token=session['csrf_token'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_status = None

    if request.method == 'POST':
        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')

        registration_status = new_user(new_username, new_password)

        if "successful" in registration_status:
            return redirect(url_for('index'))

    session["csrf_token"] = secrets.token_hex(16)
    return render_template(
        'register.html',
        title='Register',
        registration_status=registration_status,
        csrf_token=session['csrf_token']
    )

@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session data and redirect to the login page
    session.clear()
    return redirect(url_for('index'))


@app.route('/user_home', methods=['GET', 'POST'])
def user_home():
    if 'username' not in session:
        # Redirect to the login page or handle unauthorized access
        return redirect(url_for('index'))

    username = session['username']
    user_id = get_user_id(username)

    if request.method == 'POST':
        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)

        if 'check_out' in request.form:
            check_out(user_id)
        elif 'logout' in request.form:
            # Clear the session data and redirect to the login page
            session.clear()
            return redirect(url_for('index'))

    session['csrf_token'] = secrets.token_hex(16)
    return render_template('home.html', title='User Home',
                           user_id=user_id,
                           csrf_token=session['csrf_token'])

# Create a new route for attendance
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if 'username' not in session:
        return redirect(url_for('index'))

    username = session['username']
    user_id = get_user_id(username)
    if request.method == 'POST':
        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)
        tyoaika = request.form.get('tyoaika')
        tuntilaji = request.form.get('tuntilaji')
        check_in(user_id, tyoaika, tuntilaji)
        return redirect(url_for('checkin_confirmation'))

    session['csrf_token'] = secrets.token_hex(16)


    return render_template('attendance.html', title='Attendance',
                           user_id=user_id,
                           csrf_token=session['csrf_token'])

@app.route('/checkout_reason', methods=['GET', 'POST'])
def checkout_reason():
    if 'username' not in session:
        return redirect(url_for('index'))

    username = session['username']
    user_id = get_user_id(username)
    if request.method == 'POST':

        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)
        checkout_reason = request.form.get('checkout_reason')
        check_out(user_id, checkout_reason)
        return redirect(url_for('user_home'))

    session['csrf_token'] = secrets.token_hex(16)

    return render_template('checkout_reason.html',
                           title='Checkout Reason',user_id=user_id,
                           csrf_token=session['csrf_token'])


@app.route('/profile')
def user_profile():
    # Assuming the user authentication is already done
    # and the username is available in the session

    if 'username' not in session:
        # Redirect to the login page or handle unauthorized access
        return redirect(url_for('index'))

    username = session['username']
    user_id = get_user_id(username)
    attendance_history = get_user_attendance_history(user_id)

    session['csrf_token'] = secrets.token_hex(16)

    return render_template(
        'profile.html',
        title='User Profile',
        username=username,
        attendance_history=attendance_history,
        csrf_token=session['csrf_token']
    )

@app.route('/leave_request', methods=['GET', 'POST'])
def leave_request():
    if 'username' not in session:
        return redirect(url_for('index'))

    username = session['username']
    user_id = get_user_id(username)

    user_leave_requests = get_user_leave_requests(user_id)

    if request.method == 'POST':

        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)

        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        reason = request.form.get('reason')

        username = session['username']
        user_id = get_user_id(username)

        create_leave_request(user_id, start_date, end_date, reason)
        return redirect(url_for('leave_request'))

    session['csrf_token'] = secrets.token_hex(16)

    return render_template('leave_request.html',
                           title='Leave Request',
                           user_leave_requests=user_leave_requests,
                           csrf_token=session['csrf_token'])


@app.route('/checkin_confirmation')
def checkin_confirmation():
    if 'username' not in session:
        # Redirect to the login page or handle unauthorized access
        return redirect(url_for('index'))
    username = session['username']
    user_id = get_user_id(username)

    attendance = get_latest_attendance(user_id)
    session['csrf_token'] = secrets.token_hex(16)

    return render_template('checkin_confirmation.html', attendance=attendance)


@app.route('/admin_dashboard',methods=['GET', 'POST'])
def admin_dashboard():
    # Check if the user is logged in and is an admin
    if 'is_admin' not in session or not session['is_admin']:
        return redirect(url_for('index'))


    if request.method == 'POST':
        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)

        if 'logout' in request.form:
            # Clear the session data and redirect to the login page
            session.clear()
            return redirect(url_for('index'))

    session['csrf_token'] = secrets.token_hex(16)

    # Get all leave requests
    leave_requests = get_all_leave_requests()

    work_history = get_all_users_work_history()

    return render_template('admin_dashboard.html',
                           title='Admin Dashboard',
                           leave_requests=leave_requests,
                           work_history=work_history,
                           csrf_token=session['csrf_token'])


@app.route('/approve_reject_leave/<int:leave_id>/<action>', methods=['POST'])
def approve_reject_leave(leave_id, action):
    # Check if the user is logged in and is an admin
    if 'is_admin' not in session or not session['is_admin']:
        return redirect(url_for('index'))

    if request.method == 'POST':
        if request.form.get('csrf_token') != session.get('csrf_token'):
            abort(403)
        if 'logout' in request.form:
            # Clear the session data and redirect to the login page
            session.clear()
            return redirect(url_for('index'))

    session['csrf_token'] = secrets.token_hex(16)
    # Perform the approval or rejection logic based on the action parameter
    if action == 'approve':
        update_leave_status(leave_id, 'Approved')
    elif action == 'reject':
        update_leave_status(leave_id, 'Rejected')


    # Redirect back to the admin dashboard
    return redirect(url_for('admin_dashboard'))
