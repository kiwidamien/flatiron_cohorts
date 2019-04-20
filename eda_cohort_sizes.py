import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

flatiron = pd.read_pickle('flatiron.pkl')

flatiron.head()

flatiron_aggregate = flatiron.set_index('created_at').resample('W').count()['forks_count']
flatiron_aggregate.head()

plt.figure(figsize=(12,6))
plt.plot(flatiron_aggregate)
plt.ylabel('num forks')
plt.title('Number of Forks created by week');

plt.savefig('figs/weekly_forks.png')
