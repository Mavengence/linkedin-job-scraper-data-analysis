import os
import pandas as pd
import logging
from selenium.webdriver.chrome.options import Options
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from linkedin_jobs_scraper.filters import RelevanceFilters, TimeFilters, TypeFilters, ExperienceLevelFilters
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics

dataset = []

def on_data(data: EventData):
    dataset.append([data.title, data.company, data.company_link, data.date, data.link, data.insights, data.description])
    #print('[ON_DATA]', data.title, data.company, data.company_link, data.date, data.link, data.insights, len(data.description))

# Fired once for each page (25 jobs)
def on_metrics(metrics: EventMetrics):
    print('[ON_METRICS]', str(metrics))

def on_error(error):
    df = pd.DataFrame(dataset, columns=["title", "company", "company_link", "date", "link", "insights", "description"])
    df.to_csv("linkedin.csv", index=False)
    print('[ON_ERROR]', error)

def on_end():
    df = pd.DataFrame(dataset, columns=["title", "company", "company_link", "date", "link", "insights", "description"])
    df.to_csv("linkedin.csv", index=False)
    print('[ON_END]')


logging.basicConfig(level = logging.INFO)

scraper = LinkedinScraper(
    chrome_executable_path=None, # Custom Chrome executable path (e.g. /foo/bar/bin/chromedriver) 
    chrome_options=None,  # Custom Chrome options here
    headless=True,  # Overrides headless mode only if chrome_options is None
    max_workers=4,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
    slow_mo=2,  # Slow down the scraper to avoid 'Too many requests 429' errors (in seconds)
    page_load_timeout=30  # Page load timeout (in seconds)    
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

queries = [
    Query(
        #query='data',
        options=QueryOptions(
            locations=['China'],            
            #apply_link = False,  # Try to extract apply link (easy applies are skipped). Default to False.
            limit=2000,
            filters=QueryFilters(              
                company_jobs_url='https://www.linkedin.com/jobs/search/?currentJobId=3212245253&f_C=2508619%2C8385439%2C3054994%2C2569590%2C77611993%2C73385276%2C894459%2C10863618%2C31382891%2C11502372%2C15243436%2C6594%2C3672712%2C2199%2C2198%2C79815486%2C11682553%2C3501525%2C3022776%2C586240%2C9491557%2C9361631%2C6681265%2C2635811%2C3354127%2C4001505%2C474207%2C614550%2C111311%2C16128109%2C37795920%2C3014532%2C11799789%2C165755%2C1667788%2C620856%2C3267408%2C3055002%2C3559892%2C3234808%2C3489623&geoId=92000000', 
                #relevance=RelevanceFilters.RECENT,
                #time=TimeFilters.ANY,
                #type=[TypeFilters.FULL_TIME],
                #experience=None,                
            )
        )
    ),
]

scraper.run(queries)