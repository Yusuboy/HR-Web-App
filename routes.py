from app import app

from flask import render_template, request, redirect, url_for, session
from user import login, new_user
from attendance import check_in, check_out, get_user_id, get_user_attendance_history


@app.route('/', methods=['GET', 'POST'])
def index():
    notification = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if login(username, password):
            return redirect(url_for('user_home'))  # Redirect to the dashboard or another page
        else:
            notification = 'Login failed. Check your username and password. If you are a new user, please register an account.'

    return render_template('index.html', title='HR-Web-APP', notification=notification)


@app.route('/register', methods=['GET', 'POST'])
def register():
    registration_status = None

    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')

        if new_user(new_username, new_password):
            registration_status = 'Registration successful! You can now log in.'
            return redirect(url_for('index')) 
        else:
            registration_status = 'Registration failed. Please choose a different username or provide a longer password.'

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
        elif 'check_in' in request.form:
            check_in(user_id)
        elif 'logout' in request.form:
            # Clear the session data and redirect to the login page
            session.clear()
            return redirect(url_for('index'))  

    return render_template('home.html', title='User Home', user_id=user_id)



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

    return render_template('profile.html', title='User Profile', username=username, attendance_history=attendance_history)