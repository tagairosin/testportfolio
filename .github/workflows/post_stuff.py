import os
import requests
from github import Github

def main():
    # this_repo = os.environ.get('GITHUB_REPOSITORY')
    # print(this_repo)
    # g = Github()
    # repo = g.get_repo(this_repo)
    # print(repo.full_name)
    # for tag in repo.get_tags():
    #     print(tag.name)
    r=requests.get("https://api.github.com/repos/tagairosin/testportfolio/releases")
    print(r.json())
if __name__ == "__main__":
    main()
