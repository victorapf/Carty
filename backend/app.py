from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/FQAs')
def FQAs():
    return render_template('FQAs.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')


if __name__ == '__main__':
    app.run(debug=True)

   