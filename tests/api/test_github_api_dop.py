import pytest

@pytest.mark.api_dop
def test_emoji(github_api):
    r = github_api.get_emojis()
    assert r['zzz'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f4a4.png?v8'

@pytest.mark.api_dop
def test_list_commit_can_be_found(github_api):
    r = github_api.get_list_commit('AnnMurga', 'special-memory')
    assert r.status_code == 200
    body = r.json()
    assert body[0]['commit']['author']['name'] == 'Anna Murga'

@pytest.mark.api_dop
def test_list_commit_cannot_be_found(github_api):
    r = github_api.get_list_commit('AnMur', 'memory')
    assert r.status_code == 404

@pytest.mark.api_dop
def test_list_commit_cannot_be_found(github_api):
    r = github_api.get_list_commit('', '')
    body = r.json()
    assert body['message'] == 'Not Found'

@pytest.mark.api_dop
def test_list_branches_for_head_commit_can_be_found(github_api):
    r = github_api.get_list_branches_for_HEAD_commit('AnnMurga', 'special-memory', 'e072bdb7ebc6bf6ef196e34559c8ff841c88af41')
    assert r.status_code == 200

@pytest.mark.api_dop
def test_list_branches_for_head_commit_cannot_be_found(github_api):
    r = github_api.get_list_branches_for_HEAD_commit('AnnMurga', 'special-memory', 'qererwedfbc6bf6ef196e34559c8ff841c88af41')
    assert r.status_code == 422

