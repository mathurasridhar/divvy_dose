from app.routes import app
from app.src.controller import gitController, bbController
from flask import Flask , jsonify
import json

app = Flask(__name__)

@app.get('/')
def home():
    return '<h1>Flask Rest API</h1>'

@app.route('/api/git=<reponame>', methods=['GET'])
def getProfileDataGit(reponame):
    response = gitController.getGithubData(reponame)
    return jsonify(response)

@app.route('/api/bb=<reponame>', methods=['GET'])
def getProfileDataBitbucket(reponame):
    response = bbController.getBBData(reponame)
    return jsonify(response)





if __name__ == '__main__':
    app.run(debug=True)
