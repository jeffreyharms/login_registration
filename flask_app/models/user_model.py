from operator import truediv
from turtle import isvisible
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.user_pass = data['user_pass']
        
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE first_name=%(first_name)s AND last_name=%(last_name)s;"    

        result = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
    
    @classmethod
    def create_account(cls, data):
        query = "INSERT INTO users( first_name, last_name, email, user_pass) "
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s , %(user_pass)s);"
        
        result = connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate_login(data):
        isValid = True
        if data['email'] == "":
            flash("Please provide your email.", "error_email")
            isValid = False
        if data['user_pass'] == "":
            flash("Please provide your password.", "error_password")
            isValid = False
        return isValid
    
    @staticmethod
    def validate_registration(data):
        isValid = true
        if data['email'] == "":
            flash("You must provide an email.""error_register_email")
            isValid = False
        if data['user_pass'] == "":
            flash("You must provide a password""error_register_password")
            isValid = False
        if data['first_name'] == "":
            flash("You must provide your first name""error_register_first_name")
            isValid = False
        if data['last_name'] == "":
            flash("You must provide your last name""error_register_last_name")
            isValid = False
        if data['confirm_pass'] != data['user_pass']:
            flash("Please reconfirm your password""error_register_password_confirm")
            isValid = False
        if data['email_confirm'] != data['email']:
            flash("Please reconfirm your email""error_register_email_confirm")
            isValid = False
        if len(data['user_pass']) < 8:
            flash("Password must be at least eight characters long.""error_register_password")
            isValid = False
        if EMAIL_REGEX.match( data['email']) == False:
            flash("Please provide a valid email.""error_register_email")
            isValid = False
        return isValid