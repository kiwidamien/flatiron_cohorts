# Flatiron cohorts

Information collected on the different flatiron cohorts.

## Layout

### Scraping

The files `01_scrape_forks`, `02_scrape_users` and `03_pickle_users` files are all for scraping files and creating copies in the `scraped_data/` folder. Note that you will need a github application registered to effectively scrape the users (this raises the limit from 60 requests/hr to 5000 requests/hr).

You should copy and paste the following information into a `.env` file in the top level directory:
```bash
client_id=XXXXXXXXXX        # your github app's client id
client_secret=XXXXXXXXXXXXX # your github app's client secret
```
Note that you don't need to run these files: you can use the EDA from the material already in `scraped_data/`

#### TODO

Initially I was ambitous and wanted to enter all the data into a MongoDB instance on AWS so it would be easily accessible. This turned into a pain, so instead I just picked the user info. I should remove the MongoDB code at some point to simplify the number of dependencies.

### Scraped data

This is where the most recent copies of the data live.

If you are on a version of Pandas before 0.24, you might find errors when you load the pickle files. Versions after 0.24 seem to work fine.

### Helper files

* `github.py`: Functions to call the Github API
* `location.py`: Function to try and clean up the user-submitted location information


## Graph of forks created by week

![](figs/weekly_forks.png)
