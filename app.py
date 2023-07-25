# My First Flask web application 

from flask import Flask, render_template, jsonify
from database import jobs_import_from_db, job_import_from_db


app = Flask(__name__)

@app.route('/')
def hello_world():
    jobs_data = jobs_import_from_db()
    return render_template('home2.html', jobs=jobs_data, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    jobs = jobs_import_from_db()
    return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
    job = job_import_from_db(id)
    if job == None:
        # return render_template('job_not_found.html')
        return "NOT FOUND, 404"
    else:
        return render_template('jobpage.html', job=job)
    # return jsonify(job)
    


if '__name__' == '__main__':
    app.run(host='0.0.0.0', debug=True)