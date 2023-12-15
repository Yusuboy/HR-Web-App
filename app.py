"""
This module initializes a Flask web application and sets a secret key.
"""

from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes
