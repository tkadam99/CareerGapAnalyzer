from app.main import analyze_texts

def test_single_job_analysis():
    resume = "Python SQL Machine Learning NLP"
    job = "Python SQL AWS Machine Learning"

    results = analyze_texts(resume, job)

    assert "Python" in results["matched_skills"]
    assert "AWS" in results["missing_skills"]
    assert results["fit_score"] > 0