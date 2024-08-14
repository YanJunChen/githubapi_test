import requests
import os

github_headers = {
    "Authorization": os.environ["GH_HDR"] ,
    "Accept": "application/vnd.github.v3+json" ,
    "X-GitHub-Api-Version" : "2022-11-28"
}

def invite_collaborator(username):
    url = os.environ["GH_INV_API"] + username
    response = requests.put(url, headers=github_headers)
    print("response.status_code = " , response.status_code)

if __name__ == "__main__":
    invite_collaborator("eikchen0713")
