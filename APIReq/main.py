import requests
from requests import *

url = "https://gitlab.com/api/v4/users/nanuchi/projects"
response = requests.get(url)
print(f"status code: {response.status_code}")
projects = response.json()

for project in projects:
    print(f"project name : {project.get('name')}")
    print(f"project URL  : {project.get('web_url')}\n")