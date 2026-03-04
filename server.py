import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

# loginhtmlcode
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        if username == 'admin' and password == 'password':
            return flask.redirect(flask.url_for('dashboard'))
        else:
            return 'Invalid username or password'
    else:
        return {
            "html-boby": """
                <div>
                    <form method="POST">
                        <label for="userId">User ID:</label>
                        <input type="number" id="userId" name="userId" required>

                        <br>
                        <label for="otp">OTP:</label>
                        <input type="number" id="otp" name="otp" required>
                        <button type="sendOTP">Send OTP</button>
                        <br>
                        <button type="submit">Login</button>
                        <br>
                    </form>
                </div>
                <script>
                    function sendOTP() {
                        const userId = document.getElementById("userId").value;
                        const xhr = new XMLHttpRequest();
                        xhr.open("POST", "/sendOTP");
                        xhr.setRequestHeader("Content-Type", "application/json");
                        xhr.send(JSON.stringify({userId}));
                        xhr.onload = function() {
                            if (xhr.status === 200) {
                                console.log(xhr.response);
                            } else {
                                console.log("Error: " + xhr.status);
                            }
                        }
                    }
                </script>
            """
            }



if __name__ == '__main__':
    app.run(debug=True, port=5000)