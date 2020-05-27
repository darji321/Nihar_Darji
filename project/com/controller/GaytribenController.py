from flask import render_template
from project import app


@app.route('/daughter/gaytriben', methods=['GET'])
def gaytriben():
    return render_template('gaytriben.html')
    
    
@app.route('/daughter/gaytriben/gaytriben_daughter', methods=['GET'])
def gaytriben_daughter():
    return render_template('gaytriben_daughter.html')

@app.route('/daughter/gaytriben/gaytriben_contact', methods=['GET'])
def gaytriben_contact():
    return render_template('gaytriben_contact.html') 