import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

if __name__ == '__main__':
    #Inbound setting in EC2 must be set up with Custom TCP Rule, Port range 8080, Source = Anywhere
    app.run(host='0.0.0.0', port=8080, debug=True)