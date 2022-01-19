import os
from github import Github

def main():
    this_repo = os.environ.get('GITHUB_REPOSITORY')
    g = Github()
    repo = g.get_repo(this_repo)
    for release in repo.get_releases():
        print(release)
if __name__ == "__main__":
    main()
