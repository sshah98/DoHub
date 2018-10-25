from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os
from sqlalchemy import exc
import hashlib



HEROKU_DB = "postgres://utjukngdvaagnt:9e3ad063a636e4cc1ed33e0cdca2ba858daf3040ee4df5e4ed21132f4c2c82f9@ec2-50-17-194-186.compute-1.amazonaws.com:5432/d47t7c5tma2rd5"

LOCAL_DB = "postgres:///scorpio"

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = HEROKU_DB
app.secret_key = "random-key"
database = psycopg2.connect(HEROKU_DB, sslmode='allow')
db = SQLAlchemy(app)
from models import *


@app.route('/', methods=['GET', 'POST'])
def home():

    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # login form
    if request.method == 'GET':
        return render_template('login.html')
    else:
        _email = request.form['email']
        _pass = hashlib.md5(request.form['pass'].encode())
        _pass = _pass.hexdigest()

        try:

            # hash the password. if the same, then login
            data = User.query.filter_by(email=_email, password=_pass).first()

            if data is not None:
                session['logged_in'] = True
                session['email'] = request.form['email']
                session['pass'] = request.form['pass']
                session['name'] = session['email'].split("@")[0]

                return redirect(url_for('home'))
            else:
                flash(Markup("<p><center>Wrong Email/Password!</center></p>"))
                return render_template('login.html')
        except:
            flash(Markup(
                "<p><center>Sorry there has been an error! Please Try Again.</center></p>"))
            return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def register():
    # registration form
    if request.method == 'GET':
        return render_template('signup.html')

    try:
        if request.method == 'POST':

            password = hashlib.md5(request.form['pass'].encode())
            hashed_pass = password.hexdigest()

            new_user = User(
                name=request.form['name'], email=request.form['email'], password=hashed_pass)

            db.session.add(new_user)
            db.session.commit()

            session['email'] = request.form['email']
            session['pass'] = request.form['pass']
            session['name'] = session['email'].split("@")[0]

            flash(Markup("<p><center>Please login now!</center></p>"))
            return render_template('login.html')

    except exc.IntegrityError:
        flash(Markup(
            "<p><center>Sorry there has been an error! Please Try Again.</center></p>"))
        return render_template("signup.html")

@app.route('/events', methods=['GET', 'POST'])
def events():

    cur = database.cursor()
    query = "SELECT * FROM users"
    cur.execute(query)
    events = list(cur.fetchall())

    return render_template("events.html",events=events)

# -------- Logout ---------------------------------------------------------- #
@app.route('/logout/')
def logout():
    # logout form
    session['logged_in'] = False
    flash(Markup("<p><center>You have logged out. Thank you!</center></p>"))
    return redirect(url_for('home'))

@app.route('/calendar')
def calendar():
    return render_template('json.html')

if __name__ == '__main__':
    app.run(debug=True)
