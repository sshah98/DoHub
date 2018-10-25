from flask import Flask, redirect, url_for, render_template, request, session, flash, Markup
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# database = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='allow')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///scorpio"


db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()