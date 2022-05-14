from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo_survey import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    print("Got POST Info")
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comments' : request.form['comments']
    }
    dojo = Dojo.create_dojo(data)
    session['id'] = dojo['id']

    return redirect('/result')

@app.route('/result')
def result():
    data = {
        'id' : session['id']
    }
    dojo = Dojo.get_dojo(data)
    print(dojo)
    return render_template("result.html", dojo = dojo)