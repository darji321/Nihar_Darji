from flask import render_template
from project import app


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/daughter', methods=['GET'])
def daughter():
    return render_template('daughter.html')


@app.route('/picture', methods=['GET'])
def picture():
    return render_template('picture.html')
    
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')