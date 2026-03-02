import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'happy message , server is running successfully the update is working '

if __name__ == '__main__':
    app.run(debug=True)
