import os
import requests
from github import Github

def main():
    this_repo = os.environ.get('VERSION')
    print(this_repo)
if __name__ == "__main__":
    main()
