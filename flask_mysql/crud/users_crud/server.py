from flask import Flask, render_template, redirect, request, url_for

from user import User

app = Flask(__name__)

@app.route("/")
def realhome():
    return redirect('/users')

# route to render all users
@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/users/new")
def new_user():
    return render_template("createuser.html")

@app.route("/users/<int:id>")
def single_user(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    print(user)
    return render_template("readone.html", user = user)

@app.route("/create", methods=['POST'])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    id = User.create_user(data)
    
    return redirect(url_for('.single_user', id = id))

@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    print(user)
    return render_template("edituser.html", user = user)

@app.route("/users/<int:id>/edit/processing", methods=['POST'])
def process_edit(id):
    data = {
        "id" : id,
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }

    User.update_user(data)

    return redirect(url_for('.single_user', id = id))

@app.route('/delete/<int:id>')
def destroy(id):
    data = {
        'id' : id
    }

    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)