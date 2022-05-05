from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:row>')
@app.route('/<int:row>/<int:col>')
@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def index(row = 8, col = 8, color1 = 'red', color2 = 'black'):
    return render_template('index.html', row=row, col=col, lightColor = color1, darkColor = color2)


if __name__=="__main__":
    app.run(debug=True)