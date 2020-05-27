from flask import render_template
from project import app


@app.route('/daughter/vimdaben', methods=['GET'])
def vimdaben():
    return render_template('vimdaben.html')

@app.route('/daughter/vimdaben/vimdaben_children', methods=['GET'])
def vimdaben_children():
    return render_template('vimdaben_children.html')

@app.route('/daughter/vimdaben/vimdaben_contact', methods=['GET'])
def vimdaben_contact():
    return render_template('vimdaben_contact.html')    
    
@app.route('/daughter/vimdaben/vimdaben_children/hitesh')
def hitesh():
    return render_template('hitesh.html')

@app.route('/daughter/vimdaben/vimdaben_children/jignasha')
def jignasha():
    return render_template('jignasha.html')

@app.route('/daughter/vimdaben/vimdaben_children/rashmi')
def rashmi():
    return render_template('rashmi.html')  
    
@app.route('/daughter/vimdaben/vimdaben_children/hiral')
def hiral():
    return render_template('hiral.html')    