from flask import Flask
app = Flask(__name__)
app.secret_key = "puzzles"
DATABASE = "login_registration_schema"