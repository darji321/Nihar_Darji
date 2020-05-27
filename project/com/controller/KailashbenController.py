from flask import render_template
from project import app


@app.route('/daughter/kailashben', methods=['GET'])
def kailashben():
    return render_template('kailashben.html')
    
@app.route('/daughter/kailashben/kailashben_children', methods=['GET'])
def kailashben_children():
    return render_template('kailashben_children.html')

@app.route('/daughter/kailashben/kailashben_contact', methods=['GET'])
def kailashben_contact():
    return render_template('kailashben_contact.html')    
    
@app.route('/daughter/kailashben/kailashben_children/ritesh', methods=['GET'])
def ritesh():
    return render_template('ritesh.html')

@app.route('/daughter/kailashben/kailashben_children/kushboo', methods=['GET'])
def kushboo():
    return render_template('kushboo.html')