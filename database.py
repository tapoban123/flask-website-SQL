from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


load_dotenv('.env')

USER = os.environ.get('DB_USERNAME')
PASSWORD = os.environ.get('PASSWORD')
DB_NAME =os.environ.get('DB_NAME')
HOST = os.environ.get('HOST')

connectionString = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}?charset=utf8mb4'

engine = create_engine(connectionString, connect_args={
    'ssl': {
        'ssl_ca': "/etc/ssl/cert.pem"
    }
})

def jobs_import_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM JOBS;"))
        jobs = result.all()
    
    job_infos = []
    for rec in jobs:
        job_infos.append(dict(ID=rec[0], Title=rec[1], Location=rec[2], Salary=rec[3], Currency=rec[4], Responsibilities=rec[5], Requirements=rec[6]))
    return job_infos

# with engine.connect() as conn:
#     result = conn.execute(text('SELECT * FROM JOBS;'))
#     data = result.all()
#     # print(result.all(0))
# job_infos = []
# for rec in data:
#     job_infos.append(rec)

