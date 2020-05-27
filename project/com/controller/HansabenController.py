from flask import render_template
from project import app


@app.route('/daughter/hansaben', methods=['GET'])
def hansaben():
    return render_template('hansaben.html')

@app.route('/daughter/hansaben/hansaben_children', methods=['GET'])
def hansaben_children():
    return render_template('hansaben_children.html')

@app.route('/daughter/hansaben/hansaben_contact', methods=['GET'])
def hansaben_contact():
    return render_template('hansaben_contact.html') 
    
@app.route('/daughter/hansaben/hansaben_children/jignesh', methods=['GET'])
def jignesh():
    return render_template('jignesh.html')

@app.route('/daughter/hansaben/hansaben_children/nirav', methods=['GET'])
def nirav():
    return render_template('nirav.html')