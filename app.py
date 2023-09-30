from flask import Flask
app = Flask(__name__)
print(type (app))
@app.route("/hello")
def hello_world():
    return "<p>hello,world!</p>"

if __name__ == '__main__':
    app.run()