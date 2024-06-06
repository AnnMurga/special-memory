import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_none_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Additional tests for GitHub Emojis and List Commits


@pytest.mark.api_add
def test_emoji(github_api):
    r = github_api.get_emojis()

    assert (r["zzz"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f4a4.png?v8")


@pytest.mark.api_add
def test_list_commit_can_be_found(github_api):
    r = github_api.get_list_commit("AnnMurga", "special-memory")
    body = r.json()

    assert r.status_code == 200
    assert body[0]["commit"]["author"]["name"] == "AnnMurga"


@pytest.mark.api_add
def test_list_commit_cannot_be_found(github_api):
    r = github_api.get_list_commit("AnMur", "memory")

    assert r.status_code == 404


@pytest.mark.api_add
def test_list_commit_cannot_be_found(github_api):
    r = github_api.get_list_commit("", "")
    body = r.json()

    assert body["message"] == "Not Found"


@pytest.mark.api_add
def test_list_branches_for_head_commit_can_be_found(github_api):
    r = github_api.get_list_branches_for_HEAD_commit("AnnMurga", "special-memory", "e072bdb7ebc6bf6ef196e34559c8ff841c88af41")

    assert r.status_code == 200


@pytest.mark.api_add
def test_list_branches_for_head_commit_cannot_be_found(github_api):
    r = github_api.get_list_branches_for_HEAD_commit("AnnMurga", "special-memory", "qererwedfbc6bf6ef196e34559c8ff841c88af41")
    
    assert r.status_code == 422
