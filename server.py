from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page>')
def static_pages(page='index.html'):
    return render_template(page)
