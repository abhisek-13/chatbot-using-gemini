import flask
from flask import Flask,render_template,jsonify

app = Flask(__name__,template_folder="frontend\html",static_folder="frontend\css and js")

@app.route('/')
def index():
    return render_template("website.html")


if __name__ == "__main__":
    app.run(debug=True)