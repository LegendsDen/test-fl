from flask import Flask,render_template
app= Flask(__name__)


@app.route("/")
def start():
    return "Server is runing"

@app.route("/alpha")
def end():
    return render_template('index.html')


