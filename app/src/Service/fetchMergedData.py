from dotenv import load_dotenv, dotenv_values
import os
import json 
from flask import jsonify, abort
import logging
import requests
from pathlib import Path
from app.src.model.profile_model import Profile
from app.src.Service.fetchGitDao import GitHubService
from app.src.Service.fetchBBDao import BitbucketService

load_dotenv()
logging.basicConfig(filename='app/app.log', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
class MergeService:
    def __init__(self, reponame, bbreponame):
        self.reponame = reponame
        self.bbreponame = bbreponame

    def getMergedData(self):
        res = {}
        res['data'] = []
        gitObj = GitHubService(self.reponame)
        res1 = gitObj.getGitData()
        pgit = Profile()
        pgit.languages = res1.languages
        pgit.public_repos_forked = res1.public_repos_forked
        pgit.public_repos_orig = res1.public_repos_orig
        pgit.repotopics = res1.repotopics
        pgit.watcherscount = res1.watcherscount

        res1 = {}
        res1['data'] = {'githubstats':{"unforked_public_repos":pgit.public_repos_orig, "forked_public_repos":pgit.public_repos_forked, "languages":pgit.languages, "topics":pgit.repotopics, "watchers":pgit.watcherscount}}
        res['data'].append(res1['data'])
        
        bbObj = BitbucketService(self.bbreponame)
        res2 = bbObj.getBBData()
        pbb = Profile()
        pbb.languages = res2.languages
        pbb.public_repos_forked = res2.public_repos_forked
        pbb.public_repos_orig = res2.public_repos_orig
        pbb.repotopics = res2.repotopics
        pbb.watcherscount = res2.watcherscount

        res2 = {}
        res2['data'] = {'bbstats':{"unforked_public_repos":pbb.public_repos_orig, "forked_public_repos":pbb.public_repos_forked, "languages":pbb.languages, "topics":pbb.repotopics, "watchers":pbb.watcherscount}}
        res['data'].append(res2['data'])
        
        
        return res
    

