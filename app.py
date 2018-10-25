from flask import Flask, render_template, request, redirect, url_for, g, flash, session
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
