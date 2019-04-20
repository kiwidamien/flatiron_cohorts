import pandas as pd
from location import normalize_location
import matplotlib.pyplot as plt


flatiron_users = pd.read_pickle('scraped_data/userinfo.pkl')
forks = pd.read_pickle('scraped_data/flatiron.pkl')

flatiron_users.info()

flatiron_users['location'] = flatiron_users['location'].apply(normalize_location)

print(flatiron_users['location'].value_counts())


flatiron_users.head()

forks['login'] = forks['owner'].apply(lambda x: x['login'])

user_repo = flatiron_users.merge(forks, left_on='login', right_on='login', suffixes=('_user', '_repo'))
column_names = {
    'created_at_user': 'user_joined',
    'created_at_repo': 'repo_created_at',
    'updated_at': 'repo_last_updated'
}

to_drop = ['owner', '_id', 'email', 'name_user', 'full_name', 'id', 'name_repo']

user_repo = user_repo.drop(to_drop, axis=1).rename(columns=column_names)
user_repo.head(2)


user_repo['account_age_at_creation'] = user_repo.repo_created_at - user_repo.user_joined
user_repo['account_age_at_creation'].describe()

# Note that all accounts with negative times are Organizations (the is_user flag is False)
negative_time_mask = (user_repo['account_age_at_creation'].dt.total_seconds() < 0)
user_repo[negative_time_mask]


# These are in fact all the organziations!
user_repo['is_user'].value_counts()

ages = user_repo['account_age_at_creation'].dropna().dt.days
ages[ages < 356].hist(bins=100)
plt.xlim(0,300)
plt.yscale('log')
