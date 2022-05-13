from flask_app import app
from flask import render_template, redirect, request

# import the class from friend.py
from flask_app.models.friend import Friend
from flask_app.models.school import School

# route to render all friends
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    schools = School.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends, schools = schools)

# route to create a friend
@app.route("/create", methods=['POST'])
def create_friend():
    data = {
        "school_id" : request.form['school_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "occupation" : request.form['occupation']
    }

    Friend.create_friend(data)

    return redirect('/')

# route to render the update form
@app.route("/renderUpdate/<int:id>")
def render_update(id):


    return render_template ("update.html", id = id)

# processing route to update a friend
@app.route("/update", methods=['POST'])
def update_friend():
    data = {
        "id" : request.form['id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "occupation" : request.form['occupation']
    }

    Friend.update_friend(data)

    return redirect('/')

# route to delete friend
@app.route("/delete/<int:id>")
def delete(id):
    data = {
        'id' : id
    }

    Friend.destroy(data)

    return redirect('/')

@app.route("/oneschool/<int:id>")
def one_school_with_friends(id):
    data = {
        'id' : id
    }
    school = School.get_school_with_friends(data)

    return render_template("oneschool.html", one_school = school)