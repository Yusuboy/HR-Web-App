from app import app

from flask import render_template, request, redirect, url_for, flash
from user import login, new_user

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['POST'])
def login_route():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if login(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html', title='Login')

@app.route('/register', methods=['POST'])
def register_route():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if new_user(username, password):
            flash('Registration successful!', 'success')
            return redirect(url_for('login_route'))
        else:
            flash('Registration failed. Username may already exist or password is too short.', 'danger')

    return render_template('register.html', title='Register')