import pandas as pd
from pymongo import MongoClient
import time
import os

from github import get_user_info

try:
    flatiron = pd.read_pickle('scraped_data/flatiron.pkl')
except FileNotFoundError:
    print("Run 01_scrape_forks.py first -- cannot find pickle file")
    os.exit(1)

client = MongoClient()
db = client.flatiron
userinfo_collection = db.userinfo

for index, row in flatiron.iterrows():
    fork_owner = row['owner']
    if not fork_owner.get('login'):
        continue
    login = fork_owner['login']
    if userinfo_collection.find_one({'login': login}):
        print(f'duplicate for {login}')
        continue
    user_doc = get_user_info(login)
    time.sleep(0.5)
    if not user_doc:
        print(f'Something went wrong getting info for {login}')
    else:
        userinfo_collection.insert_one(user_doc)
    if index % 10 == 0:
        print(f'Processed {index} out of {len(flatiron)} users')
