import requests

class GitHub:

    def get_user(self, username):
        r = requests.get(f'http://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(f'http://api.github.com/search/repositories',
            params={"q":name}
        )
        body = r.json()

        return body
    
    def get_emojis(self):
        r = requests.get('https://api.github.com/emojis')
        body = r.json()

        return body
    
    def get_list_commit(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')

        return r
    
    def get_list_branches_for_HEAD_commit(self, owner, repo, commit_sha):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head')

        return r