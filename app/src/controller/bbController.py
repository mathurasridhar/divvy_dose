from app.src.Service.fetchBBDao import BitbucketService
import json

def getBBData(reponame):
    bb = BitbucketService(reponame)
    response = bb.getBBData()
    res = {}
    res['data'] = [{"unforked_public_repos":response.public_repos_orig, "forked_public_repos":response.public_repos_forked, "languages":response.languages, "topics":response.repotopics, "watchers":response.watcherscount}]
    return res
    