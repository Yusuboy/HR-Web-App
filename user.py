from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from db import db



def login(username, password):
    if len(username) == 0 or len(password) == 0:
        return "Username and password are required."

    query = text("SELECT id, username, password FROM Users WHERE username=:username")
    user = db.session.execute(query, {"username": username}).first()

    if user is None:
        return "Login failed. Check your username and password."

    hash_value = user.password
    if check_password_hash(hash_value, password):
        session["username"] = username
        return "Login successful!"
    else:
        return "Login failed. Check your username and password."

def new_user(username, password):
    if username.isspace() or password.isspace():
        return "Registration failed. Username and password are required for registration."
    
    if len(password) < 5:
        return "Registration failed. Please choose a password with at least 5 characters."


    query = text("SELECT id, username, password FROM Users WHERE username=:username")
    existing_user = db.session.execute(query, {"username": username}).first()

    if existing_user:
        return "Registration failed. Username already exists. Please choose a different username."

    hash_value = generate_password_hash(password)
    query = text("INSERT INTO Users (username, password) VALUES (:username, :password)")
 
    try:
        db.session.execute(query, {"username": username, "password": hash_value})
        db.session.commit()
        return "Registration successful! You can now log in."
    except Exception as e:
        print(f"Error creating new user: {e}")
        db.session.rollback()
        return "Registration failed. An error occurred while creating your account."
