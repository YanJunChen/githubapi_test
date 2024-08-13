import requests
import os

github_headers = {
    "Authorization": os.environ["GH_HDR"] ,
    "Accept": "application/vnd.github.v3+json"
}

def invite_collaborator(username):
    url = f'https://api.github.com/repos/githubapi_test/collaborators/{username}'

    response = requests.put(url, headers=github_headers)
    print("response.status_code = " , response.status_code)

    if response.status_code == 201:
        print(f'Successfully invited.')
    elif response.status_code == 204:
        print(f'{username} is a collaborator.')
    else:
        print(f'Failed to invite {username}. Response: {response.status_code} - {response.json()}')

if __name__ == "__main__":
    print(github_headers)
    invite_collaborator("eikchen0713")
