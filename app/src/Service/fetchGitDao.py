from dotenv import load_dotenv, dotenv_values
import os
import json 
from flask import jsonify, abort
import logging
import requests
from pathlib import Path
from app.src.model.profile_model import Profile

load_dotenv()

class GitHubService:
    def __init__(self, reponame):
        self.reponame = reponame

    def getGitData(self):
        api_url = os.environ.get('GITHUB_API_URL')
        url_git ='https://api.github.com/orgs/'+self.reponame + '/repos'
        pm = Profile()
        response = requests.get(url_git)
        data = response.json()
        print('Data:', data)
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
            abort(response.status_code,response.text)
    

