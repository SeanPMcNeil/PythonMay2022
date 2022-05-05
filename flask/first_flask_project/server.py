from flask import Flask
# imports the class Flask so we can use it

app = Flask(__name__)
# creates an instance of Flask that runs when the server runs

@app.route('/')
def index():
    return "hello world :D"


@app.route('/another_route')
def another_route():
    return "This is another route!!!! :)"

@app.route('/test/<route_data>')
def test_data(route_data):
    return f"Here's your data: {route_data}"

@app.route('/multiply/<int:x>/<int:y>')
def multiply(x, y):
    return f"The result of {x} and {y} is {x * y}"

# if I run this file do "this"
if __name__ == "__main__":
    app.run(debug=True) #can specify a port after debug with port="number"