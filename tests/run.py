from app.main import analyze_resume_vs_job_from_files

results = analyze_resume_vs_job_from_files()

print("\n=== Career Gap Analysis ===")
print(f"Resume Skills: {results['resume_skills']}")
print(f"Job Skills: {results['job_skills']}")
print(f"Matched Skills: {results['matched_skills']}")
print(f"Missing Skills: {results['missing_skills']}")
print(f"Extra Skills: {results['extra_skills']}")
print(f"Fit Score: {results['fit_score']}%")
print(f"Category: {results['fit_category']}")
print("Recommendations:")
for rec in results["recommendations"]:
    print(f"- {rec}")