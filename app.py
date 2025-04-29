import streamlit as st
import pdfplumber
import pickle
import re
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
from textstat import flesch_reading_ease


clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
salary_model = pickle.load(open('salary_model.pkl', 'rb'))


def clean_resume(text):
    return re.sub(r'\W+', ' ', text)


def extract_experience(text):
    match = re.search(r'(\d+)\+?\s+years?', text.lower())
    return int(match.group(1)) if match else 0


def categorize_experience(years):
    if years <= 2:
        return "Entry-Level"
    elif 3 <= 6:
        return "Mid-Level"
    else:
        return "Senior-Level"


def plagiarism_score(resume_text, existing_resumes):
    return max(fuzz.ratio(resume_text, sample) for sample in existing_resumes)


def resume_match_score(resume_vector, job_vector):
    return round(cosine_similarity(resume_vector, job_vector)[0][0] * 100, 2)


st.title("Job Role Matching")
uploaded_file = st.file_uploader("Upload Resume", type=['txt', 'pdf'])

if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        resume_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.name.endswith(".pdf"):
        with pdfplumber.open(uploaded_file) as pdf:
            resume_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    else:
        resume_text = "undupported file format.."

    
    cleaned_resume = clean_resume(resume_text)
    input_features = tfidf.transform([cleaned_resume])
    prediction_id = clf.predict(input_features)[0]
    
    category_mapping = {
        0: "Advocate", 1: "Arts", 2: "Automation Testing",
        6: "Data Science", 8: "DevOps Engineer", 10: "ETL Developer",
        15: "Java Developer", 20: "Python Developer", 24: "Web Designing",25:"software developer",
        5:"traine graduate Engineer",7:"Web Designing",21:"sales",22:"Civil Engineer",3:"Java Developer",
        8:"Bussiness Analyst",4:"Data Analyst",9:"SAP Developer",11:"Electrical Engineer",12:"OPerations Manager",
        13:"HR"
    }
    predicted_role = category_mapping.get(prediction_id, "Unknown")

    
    readability = flesch_reading_ease(cleaned_resume)

   
    experience_years = extract_experience(resume_text)
    experience_level = categorize_experience(experience_years)

   
    predicted_salary = salary_model.predict([[experience_years]])[0]

    
    existing_resumes = ["This is a sample resume text from an online source."]
    plagiarism = plagiarism_score(resume_text, existing_resumes)

    job_description_vector = tfidf.transform(["Looking for a Python Developer with Flask & Django"])
    match_score = resume_match_score(tfidf.transform([cleaned_resume]), job_description_vector)

    
    st.write(f"**Predicted Job Role:** {predicted_role}")
    st.write(f"**Experience Level:** {experience_level} ({experience_years} years)")
    st.write(f"**Estimated Salary:** ${predicted_salary:.2f}")
    st.write(f"**Plagiarism Score:** {plagiarism}%")
    st.write(f"**Resume Match Percentage:** {match_score}%")
