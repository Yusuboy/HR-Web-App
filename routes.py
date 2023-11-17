from app import app

from flask import render_template, request, redirect, url_for, flash
from user import login

@app.route('/', methods=['GET', 'POST'])
def index():
    notification = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if login(username, password):
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or another page
        else:
            notification = 'Login failed. Check your username and password. If you are a new user, please register an account.'

    return render_template('index.html', title='HR-Web-APP', notification=notification)


@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html', title='Register')