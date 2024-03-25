# importing the dependencies
import flask
from flask import Flask,render_template,jsonify,request
from src.gemini_chatbot import gemini_chatbot

# making flask object
app = Flask(__name__,template_folder="frontend\html",static_folder="frontend\css and js")

# connecting the .html file with flask interface
@app.route('/')
def index():
    return render_template("website.html")

# taking the input from user and giving the input to gemini model
@app.route('/result',methods=['GET','POST'])
def response():
    
    data = request.json
    prompt = data.get("prompt")
    response = gemini_chatbot(prompt)
    return jsonify({"response":response})
    

if __name__ == "__main__":
    app.run(debug=True)
    
