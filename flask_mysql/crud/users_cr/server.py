from flask import Flask, render_template, redirect, request

from user import User

app = Flask(__name__)

# route to render all users
@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/users/new")
def new_user():
    return render_template("createuser.html")

@app.route("/create", methods=['POST'])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.create_user(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)