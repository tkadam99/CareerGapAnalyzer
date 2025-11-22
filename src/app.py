# app.py

import pandas as pd

# Load the CSV file into a DataFrame
jobs_file = "../data/job_skills.csv"
try:
    jobs_df = pd.read_csv(jobs_file)
    print(f"CSV file loaded {len(jobs_df)} successfully.")
except FileNotFoundError:
    print(f"Error: The file {jobs_file} was not found.")
    jobs_df = pd.DataFrame()  # Create an empty DataFrame if the file is not found
except pd.errors.EmptyDataError:
    print(f"Error: The file {jobs_file} is empty.")
    jobs_df = pd.DataFrame()  # Create an empty DataFrame if the file is empty
except pd.errors.ParserError:
    print(f"Error: The file {jobs_file} could not be parsed.")
    jobs_df = pd.DataFrame()  # Create an empty DataFrame if there is a parsing error
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    jobs_df = pd.DataFrame()  # Create an empty DataFrame for any other exceptions

# Display the first few rows of the DataFrame
print(jobs_df.head())

skills_list = [
    "Python", "SQL", "Java", "C++", "JavaScript", "Docker",
    "Kubernetes", "AWS", "Azure", "Machine Learning", "Deep Learning",
    "TensorFlow", "PyTorch", "NLP", "Data Analysis", "Spark"
]

def extract_skills(text):
    found = []
    text_lower = str(text).lower()
    for skill in skills_list:
        if skill.lower() in text_lower.lower():
            found.append(skill)
    return found

jobs_df['skills'] = jobs_df['job_skills'].apply(extract_skills)

# Load Resume CSV
resume_file = "../data/sample_resume.txt"
with open(resume_file, 'r') as file:
    resume_content = file.read()
  
# print(f"Resume content loaded successfully : {resume_content}")
skills_from_resume = ""
for line in resume_content.splitlines():
    if line.lower().startswith("skills:"):
        skills_section = line.split(":", 1)[1].strip()  # take text after "Skills:"
        break

print(f"Resume content loaded successfully : {skills_section}")


resume_skills = extract_skills(skills_section)
print(f"Extracted skills from resume: {resume_skills}")

# Match jobs based on resume skills
all_job_skills = set( skill for skills in jobs_df['skills'] for skill in skills )
matched_skills = set(resume_skills) & all_job_skills
missing_skills = all_job_skills - set(resume_skills)

print(f"Matched skills: {matched_skills}")
print(f"Missing skills: {missing_skills}")