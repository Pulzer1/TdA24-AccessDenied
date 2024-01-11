import os

from flask import Flask, render_template
from . import db

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    #return "Hello TdA :) "
    return render_template("index.html")
@app.route('/api')
def api():
    return { "secret":"The cake is a lie" }
@app.route('/lecturer')
def show_lecturer():
    return render_template("lecturer.html")


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
