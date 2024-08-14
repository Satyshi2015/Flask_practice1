from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/new")
def city():
    return "<p>Hello, Dear city! How are you people doing? </p>"

@app.route("/news")
def focus():
    return ("Please focus on your work","amazing")

if __name__=='__main__':
    app.run()
