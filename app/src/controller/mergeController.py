from app.src.Service.fetchMergedData import MergeService
import json
from flask import jsonify, make_response

def getMergedData(reponame, bbreponame):
    ms = MergeService(reponame, bbreponame)
    res = ms.getMergedData()
    print('Merge data:', res)
    return res