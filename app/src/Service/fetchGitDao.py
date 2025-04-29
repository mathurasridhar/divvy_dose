from dotenv import load_dotenv, dotenv_values
import os
import json 
from flask import jsonify, abort
import logging
import requests
from pathlib import Path
from app.src.model.profile_model import Profile

load_dotenv()
logging.basicConfig(filename='app/app.log', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
class GitHubService:
    def __init__(self, reponame):
        self.reponame = reponame

    def getGitData(self):
        api_url = os.environ.get('GITHUB_API_URL')
        url_git = api_url+self.reponame + '/repos'
        logging.info('GitHub API URL:', url_git)
        pm = Profile()
        response = requests.get(url_git)
        data = response.json()
        print('Data:', data)
        logging.info(data)
        if response.status_code == 200:
            pm.languages = []
            
            watchers = [entry['watchers_count'] for entry in data if entry['visibility'] == 'public']
            pm.watcherscount += len(watchers)
            pm.public_repos_orig = [{'repo_name':entry['name'], 'public_url': entry['html_url'], 'is_fork':entry['fork']} for entry in data if entry['visibility'] == 'public' and entry['fork'] == False]
            pm.public_repos_forked = [{'repo_name':entry['name'], 'public_url': entry['html_url'], 'is_fork':entry['fork']} for entry in data if entry['visibility'] == 'public' and entry['fork'] == True]
            pm.languages = [entry['language'] for entry in data]
            git_repo_topics = []
            git_repo_topics_1 = [git_repo_topics.extend(entry['topics']) for entry in data]
            pm.repotopics = git_repo_topics
            return pm
        else:
            logging.error(response)
            abort(response.status_code,response.text)
    

