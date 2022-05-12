from flask import Flask, render_template, redirect, request

# import the class from friend.py
from friend import Friend

app = Flask(__name__)

# route to render all friends
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

# route to create a friend
@app.route("/create", methods=['POST'])
def create_friend():
    data = {
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


if __name__ == "__main__":
    app.run(debug=True)

