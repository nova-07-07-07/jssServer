import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return "<?php echo 'Hello from PHP'; ?>"

if __name__ == '__main__':
    app.run(port=5000)