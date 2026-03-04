import flask
from flask import request, jsonify, render_template, redirect, url_for
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

# Home
@app.route('/')
def home():
    return "Server Running"

# Login Page
@app.route('/loginPage')
def loginPage():
    return render_template("login.html")

# Send OTP
@app.route('/sendOTP', methods=['POST'])
def sendOTP():
    data = request.get_json()
    userId = data.get("userId")

    print("Send OTP to:", userId)

    return jsonify({"status": "OTP Sent"})

# Login Verify
@app.route('/login', methods=['POST'])
def login():
    userId = request.form.get("userId")
    otp = request.form.get("otp")

    if userId == "1001" and otp == "1234":
        return redirect(url_for("dashboard"))
    return "Invalid OTP"

# Dashboard
@app.route('/dashboard')
def dashboard():
    return "<h1>Welcome to Dashboard</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)