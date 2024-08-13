import requests
import os

github_headers = os.environ["GH_HDR"]

def invite_collaborator(username):
    url = f'https://api.github.com/repos/microsoft/EPSO-Server-Program-Community/collaborators/{username}'

    response = requests.put(url, headers=github_headers)
    print("response.status_code = " , response.status_code)

    if response.status_code == 201:
        print(f'Successfully invited.')
    elif response.status_code == 204:
        print(f'{username} is a collaborator.')
    else:
        print(f'Failed to invite {username}. Response: {response.status_code} - {response.json()}')

if __name__ == "__main__":
    print(github_headers))
    invite_collaborator("eikchen0713")
