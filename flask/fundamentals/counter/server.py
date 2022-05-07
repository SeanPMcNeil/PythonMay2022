from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'shh its a secret'

clicks = 0

@app.route('/')
def index():
    global clicks
    if 'click' in session:
        print('click exists')
        clicks += int(session['click'])
    else:
        print('key "click" does not exist!')
        clicks += 1
    return render_template("index.html", clicks=clicks)

@app.route('/click', methods=['POST'])
def click():
    print("Got Post Info")
    print(request.form)
    session['click'] = int(request.form['click'])
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset():
    print("Resetting Click Counter")
    session.clear()
    global clicks
    clicks = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)