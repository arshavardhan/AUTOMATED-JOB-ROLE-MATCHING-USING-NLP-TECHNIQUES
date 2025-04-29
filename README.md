# 📄 AUTOMATED-JOB-ROLE-MATCHING-USING-NLP-TECHNIQUES

An intelligent, machine learning-based system to automate the screening of resumes. This project helps recruiters by automatically classifying, analyzing, and ranking candidates based on their relevance to a specific job role.

---

## 🚀 Features

- 📥 Upload resumes in **PDF** or **TXT** formats.
- 🧽 Clean and preprocess resume text using NLP techniques.
- 🧠 Classify resumes into predefined **job categories** using a **KNN classifier**.
- 📊 Extract **skills**, **qualifications**, and **years of experience**.
- 📈 Compute **resume-job match percentage** using **Cosine Similarity**.
- ⚠️ Detect **plagiarism** across resumes using **Fuzzy Matching**.
- 💻 Built with **Streamlit** for an interactive and user-friendly interface.

---

## 🧠 Technologies Used

- **Language**: Python  
- **Libraries**: 
  - `Scikit-learn`
  - `Streamlit`
  - `pdfplumber`
  - `FuzzyWuzzy`
  - `Numpy`, `Pandas`, `NLTK`

---

## 📊 How It Works

1. **Upload** a resume via the web app.
2. **Parse** and clean the resume text using `pdfplumber`.
3. **Classify** the resume into job categories using TF-IDF + KNN.
4. **Extract** skills and compute years of experience.
5. **Compare** resume with a given job description using **Cosine Similarity**.
6. **Detect** plagiarism with FuzzyWuzzy string matching.

---

## 📈 Sample Results

| Metric        | Score         |
|---------------|---------------|
| Classification Accuracy | 93%          |
| Resume Match Precision | 91%          |
| Plagiarism Detection   | >85% Similarity Identified |

---

## 💻 Running the App

```bash
# Clone the repository
git clone https://github.com/yourusername/automated-resume-screening.git
cd automated-resume-screening

# Install required packages
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

---

## 🔮 Future Improvements

- Integrate deep learning models (e.g., BERT) for better understanding.
- Add live scraping of job descriptions from portals like LinkedIn.
- Support multiple resume formats (DOCX, HTML).
- Expand classification to include more job roles.

---

## 👨‍💻 Author

**Harsha**  
Cybersecurity Enthusiast | Cloud Architect | Machine Learning Explorer  
[![LinkedIn](https://www.linkedin.com/in/harsha-vardhan-dumpa-862082233/)  
[![GitHub](https://arshavardhan.github.io/portfolio/)

---
