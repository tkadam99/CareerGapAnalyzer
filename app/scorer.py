def calculate_fit_score(matched_skills, job_skills):
    if not job_skills:
        return 0.0

    return round((len(matched_skills) / len(job_skills)) * 100, 2)


def calculate_weighted_fit_score(matched_skills, market_skill_frequency):
    if not market_skill_frequency:
        return 0.0

    total_weight = sum(market_skill_frequency.values())
    matched_weight = sum(
        freq for skill, freq in market_skill_frequency.items()
        if skill in matched_skills
    )

    return round((matched_weight / total_weight) * 100, 2)


def categorize_score(score):
    if score >= 80:
        return "Strong Match"
    if score >= 60:
        return "Moderate Match"
    return "Weak Match"