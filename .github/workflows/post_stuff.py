import os
import requests

def main():
    this_repo = os.environ.get('VERSION')
    print(this_repo)
if __name__ == "__main__":
    main()
