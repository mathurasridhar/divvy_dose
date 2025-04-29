import unittest 
from unittest.mock import patch, MagicMock
import pytest
import requests
from app.src.controller.gitController import getGithubData
from app.src.controller.bbController import getBBData
from app.src.controller.mergeController import getMergedData

@pytest.mark.parametrize("reponame", [("mailchimp")])
def test_giturlsuccesspayloadcheck(reponame):
    res = getGithubData(reponame)
    result = res['data']
    result = result[0]
    rlist = list(result.keys())
    assert rlist == ['unforked_public_repos', 'forked_public_repos', 'languages', 'topics', 'watchers']

@pytest.mark.parametrize("reponame", [("mailchimp")])
def test_bburlsuccesspayloadcheck(reponame):
    res = getBBData(reponame)
    result = res['data']
    result = result[0]
    rlist = list(result.keys())
    assert rlist == ['unforked_public_repos', 'forked_public_repos', 'languages', 'topics', 'watchers']



@pytest.mark.parametrize("reponame", [("mailchi")])
def test_giturlerrorpayloadcheck(reponame):
    res = getGithubData(reponame)
    result = res['data']
    result = result[0]
    rlist = list(result.keys())
    assert rlist == ['unforked_public_repos', 'forked_public_repos', 'languages', 'topics', 'watchers']

@pytest.mark.parametrize("reponame", [("mailchi")])
def test_bburlerrorpayloadcheck(reponame):
    res = getBBData(reponame)
    result = res['data']
    result = result[0]
    rlist = list(result.keys())
    assert rlist == ['unforked_public_repos', 'forked_public_repos', 'languages', 'topics', 'watchers']

@pytest.mark.parametrize("reponame, bbrepo", [("mailchimp", "mailchimp")])
def test_mergepayloadcheck(reponame, bbrepo):
    res = getMergedData(reponame, bbrepo)
    assert len(res['data']) == 2



    