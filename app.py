# My First Flask web application 

from flask import Flask, render_template, jsonify
from database import jobs_import_from_db



app = Flask(__name__)




@app.route('/')
def hello_world():
    jobs_data = jobs_import_from_db()
    return render_template('home2.html', jobs=jobs_data, company_name='Jovian')



if '__name__' == '__main__':
    app.run(host='0.0.0.0', debug=True)