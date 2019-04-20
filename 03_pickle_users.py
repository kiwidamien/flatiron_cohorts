"""
This file makes it easier to pass data amongst users for analysis, instead of having
to create a central Mongo DB for everyone to connect to.
"""
import pandas as pd
from pymongo import MongoClient

client = MongoClient()
db = client.flatiron

flatiron_users = pd.DataFrame(db.userinfo.find())
flatiron_users.created_at = pd.to_datetime(flatiron_users.created_at)
flatiron_users['is_user'] = (flatiron_users.type == 'User')
flatiron_users.drop('type', axis=1, inplace=True)

flatiron_users.to_pickle('scraped_data/userinfo.pkl')
