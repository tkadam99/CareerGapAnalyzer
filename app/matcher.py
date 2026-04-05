def match_skills(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched = sorted(resume_set & job_set)
    missing = sorted(job_set - resume_set)
    extra = sorted(resume_set - job_set)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "extra_skills": extra,
    }