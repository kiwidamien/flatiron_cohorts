import requests
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

user = 'learn-co-students'
repo = 'python-variables-lab-data-science-intro-000'
BASE_API_URL = 'https://api.github.com'
FORK_KEYS = ['id', 'name', 'full_name', 'owner', 'created_at', 'updated_at', 'forks_count']

def list_all_repos(username):
    url = f'{BASE_API_URL}/users/{username}/repos'
    return requests.get(url).json()

def get_forks_page(username, reponame, page_number, delay=0.5, max_retries=3):
    url = f'{BASE_API_URL}/repos/{username}/{reponame}/forks?per_page=100&page={page_number}'
    for attempt in range(max_retries):
        time.sleep(delay)
        response = requests.get(url)
        if 200 <= response.status_code < 300:
            return response.json()
    return None

def get_user_info(username):
    url = f'{BASE_API_URL}/users/{username}?client_id={client_id}&client_secret={client_secret}'
    desired_fields = ['login', 'name', 'location', 'created_at', 'public_repos', 'followers', 'following',
                      'type', 'company', 'email']
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        user_data = response.json()
        return {field: user_data.get(field) for field in desired_fields}
    return None

def get_all_forks(username, reponame):
    page = 1
    while True:
        result = get_forks_page(username, reponame, page)
        print(page)
        if result:
            page = page + 1
            yield(result)
        else:
            return

def get_fork_list(username, reponame):
    forks = []
    for f in get_all_forks(username, reponame):
        forks.extend(f)
    return forks

def get_all_forks_short(username, reponame, only_fields=FORK_KEYS):
    list_of_forks = get_fork_list(username, reponame)
    return [{key: fork.get(key, None) for key in only_fields}
            for fork in list_of_forks]
