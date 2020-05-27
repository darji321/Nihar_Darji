from flask import render_template
from project import app


@app.route('/daughter/dharmishthaben', methods=['GET'])
def dharmishthaben():
    return render_template('dharmishthaben.html')
    
@app.route('/daughter/dharmishthaben/dharmishthaben_son', methods=['GET'])
def dharmishthaben_son():
    return render_template('dharmishthaben_son.html')

@app.route('/daughter/dharmishthaben/dharmishthaben_contact', methods=['GET'])
def dharmishthaben_contact():
    return render_template('dharmishthaben_contact.html')    
    
@app.route('/daughter/dharmishthaben/dharmishthaben_son/nihar', methods=['GET'])
def nihar():
    return render_template('nihar.html')