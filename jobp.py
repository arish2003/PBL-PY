from flask import Flask

def job_portal():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'epifhaefe feeihf'
    

    return app