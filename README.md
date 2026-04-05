# 🚀 AI-Powered Career Gap Analyzer

An intelligent system that analyzes a candidate's resume against job descriptions or the broader job market to identify skill gaps and provide actionable recommendations.

---

## 📌 Overview

Job seekers often struggle to understand how well their resumes align with job requirements. This project solves that problem by:

- Extracting skills from resumes and job descriptions
- Comparing them to identify gaps
- Computing a job-fit score
- Providing personalized recommendations
- Analyzing broader market demand using multiple job postings

---

## ✨ Features

### 🔹 Single Job Analysis
- Compare resume against a specific job description
- Identify:
  - ✅ Matched skills
  - ❌ Missing skills
  - ➕ Extra skills
- Compute:
  - Fit score (%)
  - Match category (Strong / Moderate / Weak)
- Get actionable recommendations

---

### 🔹 Market Analysis
- Compare resume against multiple job postings
- Identify:
  - High-demand skills in the market
  - Missing high-priority skills
- Compute:
  - Simple fit score
  - Weighted fit score (based on demand frequency)
- Visualize:
  - Market skill frequency
  - Skill gap distribution

---

### 🔹 Resume Input Options
- Paste resume text
- Upload `.txt` file
- Upload `.pdf` file

---

### 🔹 Data Visualization
- Skill comparison charts
- Market demand charts
- Progress bars for fit scores

---

## 🧠 How It Works

1. **Text Processing**
   - Clean and normalize resume and job text

2. **Skill Extraction**
   - Match skills using a predefined skill dictionary
   - Normalize aliases (e.g., "ml" → "Machine Learning")

3. **Skill Matching**
   - Compare resume skills with job/market skills

4. **Scoring**
   - Simple score: matched / total skills
   - Weighted score: based on market frequency

5. **Recommendations**
   - Suggest missing high-impact skills
   - Map skills to learning resources

---

## 🧪 Testing

Basic tests are included to validate:

- Single job analysis
- Market analysis pipeline

Run tests using:

```bash
python -m pytest tests/
```

---

## 🏗️ Project Structure

```
CareerGapAnalyzer/
│
├── app/
│   ├── main.py
│   ├── parser.py
│   ├── extractor.py
│   ├── matcher.py
│   ├── scorer.py
│   ├── recommender.py
│   └── preprocessor.py
│
├── ui/
│   └── streamlit_app.py
│
├── tests/
│   └── run.py
│   ├── test_market_analysis.py
│   └── test_single_job.py
│
├── data/
│   ├── sample_resume.txt
│   ├── sample_job_description.txt
│   ├── sample_jobs.csv
│   ├── skills_master.csv
│   └── learning_resources.csv
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/CareerGapAnalyzer.git
cd CareerGapAnalyzer
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. Activate environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python -m streamlit run ui/streamlit_app.py
```

Then open:
👉 [http://localhost:8501](http://localhost:8501)

---

## 📊 Example Output

### Single Job Analysis
- Resume vs Job skill comparison
- Fit Score with category
- Missing skills highlighted
- Recommendations provided

### Market Analysis
- Top in-demand skills
- Weighted fit score
- Skill demand visualization

---

## 🧪 Technologies Used

- Python
- Streamlit
- Pandas
- PDFPlumber
- NLP-inspired text processing

---

## 🎯 Key Highlights

- Modular backend architecture
- Supports real-world resume formats (PDF/TXT)
- Market-aware skill gap analysis
- Weighted scoring based on demand
- Interactive UI with visual insights

---

## 🚧 Future Improvements

- Use spaCy / BERT for advanced NLP extraction
- Add real-time job scraping (LinkedIn/Indeed APIs)
- Personalized learning path recommendations
- Resume improvement suggestions (rewrite bullets)
- Deploy as a web app (Streamlit Cloud / AWS)

---

## 👨‍💻 Author

**Tanmay Kadam**  
MS Computer Science — Binghamton University

---

## ⭐ If you found this useful

Give it a star ⭐ on GitHub!