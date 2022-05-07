from crypt import methods
from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    ts = datetime.now()
    print(request.form)
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    total_fruit = strawberry + raspberry + apple
    name = request.form['name']
    student_id = request.form['student_id']
    print(f"Charging {name} for {total_fruit} fruits")
    return render_template("checkout.html", strawberry=strawberry, raspberry=raspberry, apple=apple, total_fruit=total_fruit, name=name, student_id=student_id, ts=ts)


if __name__ == "__main__":
    app.run(debug=True)