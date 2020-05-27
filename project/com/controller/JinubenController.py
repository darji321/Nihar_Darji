from flask import render_template
from project import app


@app.route('/daughter/jinuben', methods=['GET'])
def jinuben():
    return render_template('jinuben.html')
    
    
@app.route('/daughter/jinuben/jinuben_children', methods=['GET'])
def jinuben_children():
    return render_template('jinuben_children.html')

@app.route('/daughter/jinuben/jinuben_contact', methods=['GET'])
def jinuben_contact():
    return render_template('jinuben_contact.html') 