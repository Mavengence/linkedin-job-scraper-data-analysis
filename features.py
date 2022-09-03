from nltk.corpus import stopwords

SKILL = ["machine learning", "deep learning", "nlp", "natural language processing", "mysql", "sql", "ms sql",
         "django", "mongodb","artificial intelligence", "ai","flask","robotics",
          "data structures","python","c++","c","r", "matlab","css","gitlab","git", "html",
          "github", "php", "hadoop", "data mining", "mining", "analytics", "visualization",
          "tableau", "predictive modeling", "cloud", "redshift", "database", "big data",
          "bi", "business intelligence", "presenting", "pitching", "google cloud", "cloud", "azure", "aws",
         "management", "devops", "sas", "spss", "mongodb", "numpy", "pandas", "query", "java",
         "javascript", "nosql", "sqlite", "redshift", "fraud", "recommendation", "recommender",
         "hive", "hbase", "embedded", "microcontroller", "iot", "software development", 
          "operations", "software engineering", "security", "vba", "oracle", "spark",
         "cloudera", "kubernetes", "kafka", "etl", "scikit-learn", "scikit", "pillow", "oracle", "jira", "node",
         "nodejs", "react", "reactjs", "angular", "angularjs", "matplotlib", "scala", "warehouse", "warehousing",
        "vba", "alteryx", "qlik", "miro", "scrum", "hdfs", "s3"]

STOPWORDS = set(stopwords.words('english'))

LEVEL_INSIGHTS = [
             "entry level", "mid-senior level", "associate","executive"
            ]

JOB_TITLE = [
    "data engineer", "data scientist", "data science", "software engineer", "software developer", "software development", 
    "computer vision", "machine vision", "cloud", "data platform", "fullstack developer", "web developer", "c developer",
    "c++ developer", "java developer", "python developer", "power bi developer", "power bi",
    "machine learning", "business intelligence", "data analyst", "analyst", "big data", "research engineer",
    "business consultant", "consultant", "operations", "analyst", "technician", "developer", "analysis",
    "security", "application", "tableau", "robotic", "test automation", "automation"
]

EDUCATION = [
            'doctor', 'doctoral', 'phd', 'ph.d.', 'ph d',
            'master', 'masters', 'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'bachelor', 'bachelors', 'BE','B.E.', 'B.E', 'BS', 'B.S', 
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH', 
        ]

DATA_SCIENCE_JOBS = ["data scientist", "computer vision", "machine learning"]

DEV_OPS_JOBS = ["software engineer","software developer", "software development", "cloud","java developer", 
                "python developer","developer","application""automation"]

DATA_ENGINEERING_JOBS = ["data engineer", "data platform", "big data"]