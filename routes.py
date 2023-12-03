from app import app

from flask import render_template, request, redirect, url_for, session
from user import login, new_user
from attendance import check_in, check_out, get_user_id, get_user_attendance_history, get_latest_attendance
from leave import create_leave_request

@app.route('/', methods=['GET', 'POST'])
def index():
    notification = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        notification = login(username, password)

        if "successful" in notification:
            return redirect(url_for('user_home'))

    return render_template('index.html', title='HR-Web-APP', notification=notification)


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_status = None

    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')

        registration_status = new_user(new_username, new_password)

        if "successful" in registration_status:
            return redirect(url_for('index'))

    return render_template('register.html', title='Register', registration_status=registration_status)



@app.route('/user_home', methods=['GET', 'POST'])
def user_home():
    if 'username' not in session:
        # Redirect to the login page or handle unauthorized access
        return redirect(url_for('login')) 

    username = session['username']
    user_id = get_user_id(username)
    
    if request.method == 'POST':
        if 'check_out' in request.form:
            check_out(user_id)
        elif 'logout' in request.form:
            # Clear the session data and redirect to the login page
            session.clear()
            return redirect(url_for('index'))  

    return render_template('home.html', title='User Home', user_id=user_id)

# Create a new route for attendance
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user_id = get_user_id(username)
    if request.method == 'POST':
        tyoaika = request.form.get('tyoaika')
        tuntilaji = request.form.get('tuntilaji')
        check_in(user_id, tyoaika, tuntilaji)
        return redirect(url_for('checkin_confirmation'))
    
    return render_template('attendance.html', title='Attendance', user_id=user_id)

@app.route('/checkout_reason', methods=['GET', 'POST'])
def checkout_reason():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user_id = get_user_id(username)
    if request.method == 'POST':
        checkout_reason = request.form.get('checkout_reason')
        check_out(user_id, checkout_reason)
        return redirect(url_for('user_home'))


    return render_template('checkout_reason.html', title='Checkout Reason',user_id=user_id)


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

    # print(attendance_history)

    return render_template('profile.html', title='User Profile', username=username, attendance_history=attendance_history)

@app.route('/leave_request', methods=['GET', 'POST'])
def leave_request():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user_id = get_user_id(username)

    if request.method == 'POST':
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        reason = request.form.get('reason')
        
        username = session['username']
        user_id = get_user_id(username)

        create_leave_request(user_id, start_date, end_date, reason)

    return render_template('leave_request.html', title='Leave Request')


@app.route('/checkin_confirmation')
def checkin_confirmation():
    if 'username' not in session:
        # Redirect to the login page or handle unauthorized access
        return redirect(url_for('index')) 
    username = session['username']
    user_id = get_user_id(username)

    attendance = get_latest_attendance(user_id)
    # print(attendance)
    return render_template('checkin_confirmation.html', attendance=attendance)
