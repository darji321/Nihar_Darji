from flask import render_template
from project import app


@app.route('/daughter/niruben', methods=['GET'])
def niruben():
    return render_template('niruben.html')

@app.route('/daughter/niruben/niruben_children', methods=['GET'])
def niruben_children():
    return render_template('niruben_children.html')

@app.route('/daughter/niruben/niruben_contact', methods=['GET'])
def niruben_contact():
    return render_template('niruben_contact.html')    
    
@app.route('/daughter/niruben/niruben_children/chetan')
def chetan():
    return render_template('chetan.html')

@app.route('/daughter/niruben/niruben_children/hiren')
def hiren():
    return render_template('hiren.html')