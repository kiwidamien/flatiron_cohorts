import pandas as pd
from pymongo import MongoClient

client = MongoClient()
db = client.flatiron

flatiron_users = pd.DataFrame(db.userinfo.find())
flatiron_users.info()

flatiron_users['location'].value_counts()


flatiron_users.head()

flatiron_users.type.value_counts()

flatiron_users.drop('type', axis=1)
