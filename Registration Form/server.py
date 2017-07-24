from flask import Flask, redirect, request, session, flash, render_template
import re

app = Flask(__name__)
app.secret_key = 'very secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'.*?[A-Z]+.*?[0-9]+|.*?[0-9]+.*?[A-Z]')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods = ['POST'])
def user():
    data = request.form

    errors = []

    if not data['first_name'] or not data['last_name'] or not data['email'] or not data['password']:
        errors.append('All fields are required')
    elif not EMAIL_REGEX.match(data['email']):
        errors.append('Invalid email address')
    elif len(data['password']) < 7:
        errors.append('Password must be at least 8 characters')
    elif not PASSWORD.match(data['password']):
        errors.append('Password must contain at least 1 capital and one number')


    if not data['password'] == data['confirm_password']:
        errors.append('Password and Password confirmation must match')

    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    return render_template('result.html')


app.run(debug=True)
