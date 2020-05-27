from flask import render_template
from project import app


@app.route('/daughter/apekshaben', methods=['GET'])
def apekshaben():
    return render_template('apekshaben.html')
    
@app.route('/daughter/apekshaben/apekshaben_children', methods=['GET'])
def apekshaben_children():
    return render_template('apekshaben_children.html')

@app.route('/daughter/apekshaben/apekshaben_contact', methods=['GET'])
def apekshaben_contact():
    return render_template('apekshaben_contact.html')    
    
@app.route('/daughter/apekshaben/apekshaben_children/yash', methods=['GET'])
def yash():
    return render_template('yash.html')