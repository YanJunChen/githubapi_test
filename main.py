import requests
import os

github_headers = {
    "Authorization": os.environ["GH_HDR"] ,
};

def invite_collaborator(username):
    url = os.environ["GH_INV_API"] + username;
    response = requests.put(url, headers=github_headers);
    print(response.status_code);

invite_collaborator("eikchen0713");
