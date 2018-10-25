from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# database = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='allow')


# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///scorpio"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://utjukngdvaagnt:9e3ad063a636e4cc1ed33e0cdca2ba858daf3040ee4df5e4ed21132f4c2c82f9@ec2-50-17-194-186.compute-1.amazonaws.com:5432/d47t7c5tma2rd5"


# database = psycopg2.connect("postgres:///scorpio", sslmode='allow')
# database = psycopg2.connect

database = psycopg2.connect(
    'postgres://utjukngdvaagnt:9e3ad063a636e4cc1ed33e0cdca2ba858daf3040ee4df5e4ed21132f4c2c82f9@ec2-50-17-194-186.compute-1.amazonaws.com:5432/d47t7c5tma2rd5')

db = SQLAlchemy(app)
from models import *


@app.route('/')
def hello():
	print(database)
	return "{}".format("Hello World")

if __name__ == '__main__':
    app.run(debug=True)