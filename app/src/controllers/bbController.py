mergeddata = []
from app.src.Service import fetchBBDao

def getBBData(reponame):
    response = fetchBBDao.getBBData(reponame)
    return response