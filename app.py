from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# database = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='allow')


app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///scorpio"

database = psycopg2.connect("postgres:///scorpio", sslmode='allow')
# database = psycopg2.connect

db = SQLAlchemy(app)
from models import *


@app.route('/')
def hello():
	print(database)
	return "{}".format("Hello World")

if __name__ == '__main__':
    app.run(debug=True)