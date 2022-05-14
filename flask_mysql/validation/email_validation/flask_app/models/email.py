from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_val_schema').query_db(query)
        emails = []

        for email in results:
            emails.append(cls(email))

        return emails

    @classmethod
    def create_email(cls,data):
        flash('The email address you entered is VALID! Thank you!')
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL('email_val_schema').query_db(query, data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL('email_val_schema').query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('email_val_schema').query_db(query, email)
        if len(results) >= 1:
            flash('Email is already registered')
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash('Invalid email address!')
            is_valid = False
        
        return is_valid
