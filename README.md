<div style="background-color:white">
  <div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/de/3/31/Bosch-logotype.svg" width="200">    
    <h1 style="color:black">Bosch LinkedIn Scraper - Data Analysis</h1> 
    <h3 style="color:black">Tim Löhr<h3>
  </div>
  <hr>
</div>

## Links to Ressources

- [linkedin_jobs_scraper](https://github.com/spinlud/py-linkedin-jobs-scraper)

### Repository Structure
------------
    
    ├── (1) Data_Analysis.ipynb                             <- All of the analysis lies here
    │
    ├── (2) data_analysis.py                                <- All of the used functions are here                                          
    │
    |── (3) features.py                                     <- All of the listed used for dataset building lies here
    │       
    ├── (4) linkedin_jobs_scraper.py                        <- The scripts that scraps the jobs and builds the csv file         
    │
    │── (5) _secrets.py                                     <- Contains the username and token for the plotly graphics upload
    │
    ├── linkedin_all_jobs.csv                               <- Contains the scraped data
    ├── envirnment.yml  
    ├── example.png 
    ├── .gitignore 
    └── README.md   

--------

### Abstract

This projects to identify what skills companies require for certain job positions differentiated by the level of the position, such as entry-level or senior-level. For this purpose, the company Robert Bosch in Germany was picked together with the jobs data scientist, devops engineers and data engineers. Ternary plots identify which skills among these three jobs are intersecting, but also differentiating from each other. A CV and cover letter can be optimized with the awareness of a possible company techstack. 

### Example

![](https://github.com/mavengence/linkedin-job-scraper-data-analysis/example.png)

### Built With

* [Python 3.9.12](https://www.python.org/downloads/)
* all following steps are for *macOS*, steps for *Windows* or *Linux* may differ

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3

```sh
# Install via brew on macOS
brew install python
```

For Linux and Windows refer to [this](https://realpython.com/installing-python/).

### Installation

* Clone the repository
* Install conda
* Install environment.yml

```sh
# Run this at repository root
conda env create -f environment.yml
```

* Run the scraper
* Get the cookie from your LinkedIn profile, as shown [here](https://github.com/spinlud/py-linkedin-jobs-scraper)

```sh
# Run this at repository root
LI_AT_COOKIE=XXX python linkedin_jobs_scraper.py
```

* Open the data analysis notebook

```sh
# Run this at repository root
jupyter notebook
```
