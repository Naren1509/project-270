# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below
@app.route('/login',methods=["POST"])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']
    if username == 'verify' and password == '12345':
        account_sid = 'AC44ce835f45f88a09f22c987c09f2b76b'
        auth_token = '40793737aa89a16798ed87427fa2d965'
        client = Client(account_sid,auth_token)

        verification = client.verify \
            .services('IS11499af246b933fe28d8fdde93f6ebad') \
            .verifications \
            .create(to=mobile_number, channel='sms')
        print(verification.status)
        return render_template('otp_verify.html')

    else:
        return "Entered User Id or Password is Wrong"


if __name__ == "__main__":
    app.run()

