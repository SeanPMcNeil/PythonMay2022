from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def register():
    if not Email.validate_email(request.form):
        return redirect('/')
    
    data = {
        'email' : request.form['email']
    }

    Email.create_email(data)

    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.get_all()

    return render_template("success.html", emails = emails)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/success')