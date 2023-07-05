#Configuracion inicial dpel servidor 

from flask import Flask, render_template
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)