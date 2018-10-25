from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os


HEROKU_DB = "postgres://utjukngdvaagnt:9e3ad063a636e4cc1ed33e0cdca2ba858daf3040ee4df5e4ed21132f4c2c82f9@ec2-50-17-194-186.compute-1.amazonaws.com:5432/d47t7c5tma2rd5"

LOCAL_DB = "postgres:///scorpio"

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LOCAL_DB
database = psycopg2.connect(LOCAL_DB, sslmode='allow')
db = SQLAlchemy(app)
from models import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
