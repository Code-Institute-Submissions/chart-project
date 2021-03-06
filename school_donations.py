from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

MONGODB_HOST = 'ds017248.mlab:17248'
MONGODB_PORT = 17248
DBS_NAME = 'heroku_063s6gnx'
COLLECTION_NAME = 'projects'
MONGODB_URI = os.getenv('MONGODB_URI')
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, 'primary_focus_subject': True, 'teacher_prefix': True, '_id': False}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorsUS/projects")
def donor_projects():
    connection = MongoClient(MONGODB_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=20000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects


if __name__ == "__main__":
    app.run(debug=True)