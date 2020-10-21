from flask import Flask, render_template
import sys
import os
# insert at 1, 0 is the script path (or '' in REPL)

sys.path.insert(0, '../algorithm')
from dtwBaseCode import main
sys.path.insert(0, '../MinIO')
print(sys.path)
import minio_integrate

import dtwBaseCode

"""


This is basic implementation of Flask as shown in their documentation here https://flask.palletsprojects.com/en/1.1.x/quickstart/

"""
app = Flask(__name__)

@app.route("/")
def hello():
    minio_integrate.main()
    x = dtwBaseCode.main('train.json', 'test.json')
    minio_integrate.upload('../flask/output.txt')
    os.remove('output.txt')
    return render_template('index.html', variable=x)



if __name__ == '__main__':
    app.run(debug = True )
