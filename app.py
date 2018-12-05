from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from data import Articles

app = Flask(__name__)

Articles = Articles()

# Index
@app.route('/')
def index():
    return render_template('home.html')


# About
@app.route('/about')
def about():
    return render_template('about.html')


# Articles
@app.route('/articles')
def articles():
    # Create cursor
   return render_template('articles.html', articles=Articles)

#Single Article
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
