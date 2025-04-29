import re
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from textstat import flesch_reading_ease

# Load dataset
df = pd.read_csv("C:\\Users\\dumpa\\OneDrive\\Desktop\\python\\resume\\UpdatedResumeDataSet.csv", encoding='utf-8')
# Function to clean resume text
def clean_resume(txt):
    clean_text = re.sub(r'http\S+\s', ' ', txt)  # Remove links
    clean_text = re.sub(r'RT|cc', ' ', clean_text)
    clean_text = re.sub(r'#\S+\s', ' ', clean_text)
    clean_text = re.sub(r'@\S+', '  ', clean_text)  # Remove mentions
    clean_text = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)  # Remove non-English characters
    clean_text = re.sub(r'\s+', ' ', clean_text)  # Remove extra spaces
    return clean_text

df['Resume'] = df['Resume'].apply(clean_resume)

# Extract experience
def extract_experience(text):
    match = re.search(r'(\d+)\+?\s+years?', text.lower())
    return int(match.group(1)) if match else 0

df["Years_of_Experience"] = df["Resume"].apply(extract_experience)

# Categorize experience level
def categorize_experience(years):
    if years <= 2:
        return "Entry-Level"
    elif 3 <= 6:
        return "Mid-Level"
    else:
        return "Senior-Level"

df["Experience_Category"] = df["Years_of_Experience"].apply(categorize_experience)


# TF-IDF Vectorization for Resume Matching
tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit(df["Resume"])
resume_features = tfidf.transform(df["Resume"])

# Encode target labels
le = LabelEncoder()
df["Category"] = le.fit_transform(df["Category"])

# Train Job Role Prediction Model
X_train, X_test, y_train, y_test = train_test_split(resume_features, df["Category"], test_size=0.2, random_state=42)

clf = OneVsRestClassifier(KNeighborsClassifier(n_neighbors=5))
clf.fit(X_train, y_train)

# Train Salary Prediction Model
X_salary = df[["Years_of_Experience"]]
y_salary = np.random.randint(40000, 150000, size=len(df))  # Simulated salary data
salary_model = RandomForestRegressor(n_estimators=100, random_state=42)
salary_model.fit(X_salary, y_salary)

# Save models
pickle.dump(tfidf, open("tfidf.pkl", "wb"))
pickle.dump(clf, open("clf.pkl", "wb"))
pickle.dump(salary_model, open("salary_model.pkl", "wb"))
