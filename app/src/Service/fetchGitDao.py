from dotenv import load_dotenv
import os
import json 
from flask import jsonify, abort
import logging
import requests
from pathlib import Path


def getGitData(reponame):
    url_git ='https://api.github.com/orgs/'+reponame + '/repos'
    
    response = requests.get(url_git)
    data = response.json()
    print('Data:', data)
    if response.status_code == 200:
        git_repo_languages = []
        git_watchers_count = [entry['watchers_count'] for entry in data if entry['visibility'] == 'public']
        git_repo_original_lst = [{'repo_name':entry['name'], 'public_url': entry['html_url'], 'is_fork':entry['fork']} for entry in data if entry['visibility'] == 'public' and entry['fork'] == False]
        git_repo_forked_lst = [{'repo_name':entry['name'], 'public_url': entry['html_url'], 'is_fork':entry['fork']} for entry in data if entry['visibility'] == 'public' and entry['fork'] == True]
        git_repo_languages = [entry['language'] for entry in data]
        git_repo_topics = []
        git_repo_topics_1 = [git_repo_topics.extend(entry['topics']) for entry in data]
        rres = {}
        rres['data']= [{'git_public_repos_unforked':len(git_repo_original_lst), 'git_public_repos_forked':len(git_repo_forked_lst), 'git_watchers_count':sum(git_watchers_count), 'git_repo_languages':list(set(git_repo_languages)),'git_repo_topics':list(set(git_repo_topics))}]
        return rres
    else:
        abort(response.status_code,response.text)
   

