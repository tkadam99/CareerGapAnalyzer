from app.main import analyze_resume_vs_market_from_file

def test_market_analysis():
    results = analyze_resume_vs_market_from_file()

    assert "matched_skills" in results
    assert "missing_skills" in results
    assert results["fit_score"] >= 0