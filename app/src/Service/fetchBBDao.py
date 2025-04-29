from dotenv import load_dotenv
import os
import json 
from flask import jsonify
import logging
import requests


def getBBData(reponame):
    url_bitbucket = f'https://api.bitbucket.org/2.0/repositories/{reponame}'
    try:
        response = requests.get(url_bitbucket)
        data = response.json()
        bb_public_repos = data.json()
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
        rres = {}
        rres['data'] = [{'bb_public_repos_orig':bb_repos, 'bb_forked_repos':bb_forked, 'bb_watchers':bb_watcher_cnt, 'bb_languages':len(list(set(bb_languages)))}]
        return rres
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh.args[0])

