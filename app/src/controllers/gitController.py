mergeddata = []
from app.src.Service import fetchGitDao

def getGithubData(reponame):
    response = fetchGitDao(reponame)
    return response