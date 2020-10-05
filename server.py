import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [{'title': 'Test Post #1', 'author': 'Daniel' },
            {'title': 'Test Post #2', 'author': 'Daniel'}
            ]
    return render_template('home.html', good = True, posts=posts)
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# SAMPLE SUB-PAGE
#@app.route('/blog/<string:blog_id>')
#def blogpost(blog_id):
#    return 'This is blog post number ' + blog_id

if __name__ == '__main__':
    #Inbound setting in EC2 must be set up with Custom TCP Rule, Port range 8080, Source = Anywhere
    app.run(host='0.0.0.0', port=8080, debug=True)