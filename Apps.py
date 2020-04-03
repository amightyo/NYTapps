# Dr. Itauma's HBAPLessons
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

NYT_API_KEY = os.getenv('NYT_API_KEY')


def article_lookup(Query):
    r = requests.get(
        'https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+Query+'&api-key='+NYT_API_KEY)

    return r


def article_lookup_bydate(Query, date):
    r = requests.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&facet=true&begin_date=' +
                     date+'&end_date='+date+'&api-key='+NYT_API_KEY)

    return r


# Search for any article
Query = 'covid-19'

# r = article_lookup(Query)
# packages_json = r.json()

# print(packages_json)


# Search for all documents published on April 2, 2020 containing 'covid-19'.
date = '20200401'
r = article_lookup_bydate(Query, date)
packages_json = r.json()

print(packages_json)
