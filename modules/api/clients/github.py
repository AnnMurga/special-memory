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
    