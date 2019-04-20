import pandas as pd
from github import user, repo, get_all_forks_short
import os

fork_data = get_all_forks_short(user, repo)

flatiron = pd.DataFrame(fork_data)

flatiron.created_at = pd.to_datetime(flatiron.created_at)
flatiron.updated_at = pd.to_datetime(flatiron.updated_at)

try:
    os.mkdir('scraped_data')
    print('Made scraped_data directory for data files')
except FileExistsError:
    pass

print('Putting data in the scraped_data directory')

flatiron.to_csv('scraped_data/flatiron.csv')
flatiron.to_pickle('scraped_data/flatiron.pkl')

print(f"We gave collected information on {len(flatiron)} forks")
