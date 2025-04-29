from dotenv import load_dotenv, dotenv_values
import os
import json 
from flask import jsonify, abort
import logging
import requests
from app.src.model.profile_model import Profile
load_dotenv()
logging.basicConfig(filename='app/app.log', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
class BitbucketService:
    def __init__(self, reponame):
        self.reponame = reponame
    def getBBData(self):
        api_url = os.environ.get('BITBUCKET_API_URL')
        url_bitbucket = api_url +"/"+ self.reponame
        logging.info('Bitbucket API URL:',url_bitbucket)
        response = requests.get(url_bitbucket)
        pm = Profile()
        logging.info(response)
        if response.status_code == 200:
            data = response.json()
            bb_public_repos = data
            bb_public_repos = bb_public_repos['values']
            bb_repos = []
            bb_forked = []
            bb_languages = []
            bb_watcher_cnt = 0
            for repo in bb_public_repos:
                if repo['is_private'] is False and repo['parent'] is None:
                    bb_repos.append({'name':repo['name'], 'full_name':repo['full_name']})
                    watchers = repo['links']['watchers']['href']
                    bb_languages.append(repo['language'])
                    wres = requests.get(watchers)
                    wres = wres.json()
                    bb_watcher_cnt += len(wres['values'])
                elif repo['is_private'] is False and repo['parent'] is not None:
                    bb_forked.append({'name':repo['name'], 'full_name':repo['full_name']})
                    watchers = repo['links']['watchers']['href']
                    wres = requests.get(watchers)
                    wres = wres.json()
                    bb_watcher_cnt += len(wres['values'])
                    bb_languages.append(repo['language'])
            pm.public_repos_orig = bb_repos
            pm.public_repos_forked = bb_forked
            pm.languages = bb_languages
            pm.watcherscount = bb_watcher_cnt
            pm.repotopics = []
            return pm
        else:
            logging.e(response)
            abort(response.status_code, response.text)
   

  