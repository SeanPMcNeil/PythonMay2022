from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'skdifhsakjdbnlajknbfljksjhbv'

@app.route('/')
def index():
    # if (session['guess']):
    #     pass
    # else:
    number = random.randint(1, 100)
    session['number'] = number
    print(session['number'])
    return render_template("/index.html", number = number)

@app.route('/number_guess', methods = ['POST'])
def guess_check():
    guess = int(request.form['guess'])
    print(session['number'])
    print(request.form['guess'])
    if (guess == session['number']):
        print("You are Right!")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)