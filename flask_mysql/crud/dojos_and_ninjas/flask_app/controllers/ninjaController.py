from flask_app import app
from flask import render_template, redirect, request, url_for

# import the class from friend.py
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', dojos = dojos)

@app.route('/createdojo', methods=['POST'])
def create_dojo():
    data = {
        'name' : request.form['name']
    }

    Dojo.create_dojo(data)

    return redirect('/dojos')

@app.route('/ninjas')
def ninja_form():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        "dojo_id" : request.form['dojo_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }

    Ninja.create_ninja(data)
    id = data['dojo_id']
    # Needs to redirect to single dojo page
    return redirect(url_for('.one_dojo_with_ninjas', id = id)) 

@app.route('/dojos/<int:id>')
def one_dojo_with_ninjas(id):
    data = {
        'id' : id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("onedojo.html", dojo = dojo)
