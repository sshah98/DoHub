from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/calendar')
def calendar():
    return render_template('json.html')

if __name__ == '__main__':
    app.run()
