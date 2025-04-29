from app.src.Service.fetchGitDao import GitHubService
import json
from flask import jsonify

def getGithubData(reponame):
    gs = GitHubService(reponame)
    response = gs.getGitData()
    res = {}
    res['data'] = [{"unforked_public_repos":response.public_repos_orig, "forked_public_repos":response.public_repos_forked, "languages":response.languages, "topics":response.repotopics, "watchers":response.watcherscount}]
    rstr = str(res['data'])
    
    return json.dumps(rstr)