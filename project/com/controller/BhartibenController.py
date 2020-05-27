from flask import render_template
from project import app


@app.route('/daughter/bhartiben', methods=['GET'])
def bhartiben():
    return render_template('bhartiben.html')

@app.route('/daughter/bhartiben/bhartiben_children', methods=['GET'])
def bhartiben_children():
    return render_template('bhartiben_children.html')

@app.route('/daughter/bhartiben/bhartiben_contact', methods=['GET'])
def bhartiben_contact():
    return render_template('bhartiben_contact.html')    
    
@app.route('/daughter/bhartiben/bhartiben_children/chirag', methods=['GET'])
def chirag():
    return render_template('chirag.html')