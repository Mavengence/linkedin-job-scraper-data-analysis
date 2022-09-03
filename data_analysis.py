import re
import datetime
import spacy
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

from features import *


# Spacy settings
nlp = spacy.load("en_core_web_lg")

pattern1 = [{"label": "SKILL", "pattern": skill} for skill in SKILL]
pattern2 = [{"label": "EDUCATION", "pattern": education} for education in EDUCATION]

ruler = nlp.add_pipe('entity_ruler', after="ner")
ruler.add_patterns(pattern1)
ruler.add_patterns(pattern2)


def cleaning(text):
    review = re.sub(
        '(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?"',
        " ",
        text,
    )
    review = review.lower()
    review = review.split()
    lm = WordNetLemmatizer()
    review = [
        lm.lemmatize(word)
        for word in review
        if not word in set(STOPWORDS)
    ]
    return " ".join(review)

def get_skills(text):
    doc = nlp(text)
    skills = []
    for ent in doc.ents:
        if ent.label_ == "SKILL":
            skills.append(ent.text)
    return np.array(set(list(skills)))

def get_dates(text):
    doc = nlp(text)
    dates = []
    for ent in doc.ents:
        if ent.label_ == "DATE":
            reg = re.match("([0-9] [0-9]|[0-9]) year", ent.text)
            if reg:
                return reg[0]
            
def get_minimum_year(text):
    reg = get_dates(text)
    if reg:
        return reg.split(" ")[0]
    
def get_maximum_year(text):
    reg = get_dates(text)
    if reg:
        regx = reg.split(" ")
        if len(regx) == 3:
            return regx[1]
        else:
            return get_minimum_year(text)
            
def get_education(text):
    doc = nlp(text)
    education = []
    for ent in doc.ents:
        if ent.label_ == "EDUCATION":
            education.append(ent.text)
    return list(set(list(education)))
        
def map_job_titles(title):
    title = title.lower()
    
    for job in JOB_TITLE:
        if job in title:
            if job == "data science":
                return "data scientist"
            return job    
    else:
        if title == "ae":
            return "chinese"
        elif "bigdata" in title:
                return "big data"
        else:
            return title
    
def get_insights_level(insights):
    insights = insights.lower()
    for level in LEVEL_INSIGHTS:
        if level in insights:
            return level
    if not level:
        return np.nan
    
def get_bosch_df(df):
    """
        Filter dataset by Bosch company subsidaries
    """
    bosch_list = []

    for company in df["company"].unique():
        match = re.findall("Bosch", company)
        if match:
            bosch_list.append(company)

    return df[df["company"].isin(bosch_list)].reset_index(drop=True)
    
def create_features(df):
    df["education"] = df["description"].apply(lambda x: get_education(cleaning(x)))
    df["from_yrs_exp"] = df["description"].apply(lambda x: get_minimum_year(cleaning(x)))
    df["to_yrs_exp"] = df["description"].apply(lambda x: get_maximum_year(cleaning(x)))
    df["cleaned_title"] = df["title"].apply(lambda x: map_job_titles(cleaning(x)))
    df["level"] = df["insights"].apply(lambda x: get_insights_level(x))
    df["skills"] = df["description"].apply(lambda x: get_skills(cleaning(x)))
    return df

def gantt_experience(input_df):
    """
        Prepare dataset to plot the Gantt diagram plot from Plotly
    """

    today = datetime.date.today()
    x = input_df.dropna().reset_index(drop=True)
    x["from_yrs_exp"] = x["from_yrs_exp"].astype(int)
    x["to_yrs_exp"] = x["to_yrs_exp"].astype(int)
    
    exp = x.groupby("level").mean().sort_values(by=["from_yrs_exp", "to_yrs_exp"]).reset_index()
    
    exp = exp.rename(columns={"level": "Task", "from_yrs_exp": "Start", "to_yrs_exp": "Finish"})
    
    fig = ff.create_gantt(exp)
    fig.update_layout(xaxis_type='linear')
    fig.update_layout(
        yaxis_title="Level",
        xaxis_title="Years (experience)",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    return fig
    
def make_ternary_data(df_topic):
    """
        Prepare dataset to plot the ternary plot from Plotly
    """

    df_skill = pd.DataFrame(columns=SKILL, index=["data scientist", "devops", "data engineer"]).fillna(0)
    v = {0: "data scientist", 1: "devops", 2: "data engineer"}

    for i in range(len(df_topic)):
        skills = df_topic.iloc[i]["skills"]
        job = df_topic.iloc[i]["cleaned_title"]
        for skill in skills:
            try:
                df_skill.loc[job, skill] += 1
            except:
                pass

    df_skill = df_skill.T

    df_skill = df_skill.reset_index().rename(columns={"index": "skill"})
    df_skill["total"] = df_skill[["data scientist", "devops", "data engineer"]].sum(1)
    winners = np.argmax(df_skill[["data scientist", "devops", "data engineer"]].values, 1)
    df_skill["winner"] = [v[winner] for winner in winners]
    
    return df_skill