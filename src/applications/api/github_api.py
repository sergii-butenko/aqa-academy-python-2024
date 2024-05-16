import requests


class GitHubAPIClient:

    def __init__(self) -> None:
        pass

    def search_repos(self, repo_name):
        r = requests.get(
            url=f'https://api.github.com/search/repositories?q={repo_name}',
        )
        
        data = r.json()
        return data['total_count'], r
