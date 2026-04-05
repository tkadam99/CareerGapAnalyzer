from collections import Counter

from app.config import (
    SAMPLE_RESUME_PATH,
    SAMPLE_JOB_DESCRIPTION_PATH,
    SAMPLE_JOBS_CSV_PATH,
    SKILLS_MASTER_PATH,
    LEARNING_RESOURCES_PATH,
)
from app.parser import load_text_file, load_jobs_csv
from app.preprocessor import clean_text
from app.extractor import load_skill_dictionary, extract_skills
from app.matcher import match_skills
from app.scorer import (
    calculate_fit_score,
    calculate_weighted_fit_score,
    categorize_score,
)
from app.recommender import generate_recommendations


def analyze_texts(resume_text: str, job_text: str):
    resume_text = clean_text(resume_text)
    job_text = clean_text(job_text)

    skill_map = load_skill_dictionary(SKILLS_MASTER_PATH)

    resume_skills = extract_skills(resume_text, skill_map)
    job_skills = extract_skills(job_text, skill_map)

    match_results = match_skills(resume_skills, job_skills)

    fit_score = calculate_fit_score(
        match_results["matched_skills"],
        job_skills,
    )
    fit_category = categorize_score(fit_score)

    recommendations = generate_recommendations(
        match_results["missing_skills"],
        LEARNING_RESOURCES_PATH,
    )

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": match_results["matched_skills"],
        "missing_skills": match_results["missing_skills"],
        "extra_skills": match_results["extra_skills"],
        "fit_score": fit_score,
        "fit_category": fit_category,
        "recommendations": recommendations,
    }


def analyze_resume_vs_job_from_files(
    resume_path=SAMPLE_RESUME_PATH,
    job_path=SAMPLE_JOB_DESCRIPTION_PATH,
):
    resume_text = load_text_file(resume_path)
    job_text = load_text_file(job_path)
    return analyze_texts(resume_text, job_text)


def analyze_resume_vs_market(resume_text: str, jobs_df):
    skill_map = load_skill_dictionary(SKILLS_MASTER_PATH)

    resume_text = clean_text(resume_text)
    resume_skills = extract_skills(resume_text, skill_map)

    all_job_skill_lists = []
    market_skill_counter = Counter()

    for _, row in jobs_df.iterrows():
        description = clean_text(str(row["description"]))
        job_skills = extract_skills(description, skill_map)
        all_job_skill_lists.append(job_skills)
        market_skill_counter.update(job_skills)

    market_skills = sorted(market_skill_counter.keys())

    match_results = match_skills(resume_skills, market_skills)

    fit_score = calculate_fit_score(
        match_results["matched_skills"],
        market_skills,
    )

    weighted_fit_score = calculate_weighted_fit_score(
        match_results["matched_skills"],
        market_skill_counter,
    )

    fit_category = categorize_score(weighted_fit_score)

    top_missing_skills = sorted(
        match_results["missing_skills"],
        key=lambda skill: market_skill_counter[skill],
        reverse=True
    )

    recommendations = generate_recommendations(
        top_missing_skills[:5],
        LEARNING_RESOURCES_PATH,
    )

    return {
        "resume_skills": resume_skills,
        "market_skills": market_skills,
        "matched_skills": match_results["matched_skills"],
        "missing_skills": match_results["missing_skills"],
        "extra_skills": match_results["extra_skills"],
        "fit_score": fit_score,
        "weighted_fit_score": weighted_fit_score,
        "fit_category": fit_category,
        "top_missing_skills": top_missing_skills[:5],
        "market_skill_frequency": dict(sorted(market_skill_counter.items(), key=lambda x: x[1], reverse=True)),
        "recommendations": recommendations,
    }


def analyze_resume_vs_market_from_file(
    resume_path=SAMPLE_RESUME_PATH,
    jobs_csv_path=SAMPLE_JOBS_CSV_PATH,
):
    resume_text = load_text_file(resume_path)
    jobs_df = load_jobs_csv(jobs_csv_path)
    return analyze_resume_vs_market(resume_text, jobs_df)


if __name__ == "__main__":
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