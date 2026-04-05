import pandas as pd


def generate_recommendations(missing_skills, learning_resources_path):
    if not missing_skills:
        return ["Great match. No major skill gaps detected."]

    df = pd.read_csv(learning_resources_path)
    recommendations = []

    for skill in missing_skills:
        matched_rows = df[df["skill_name"].str.lower() == skill.lower()]
        if not matched_rows.empty:
            resource_name = matched_rows.iloc[0]["resource_name"]
            recommendations.append(f"Learn {skill}: {resource_name}")
        else:
            recommendations.append(f"Consider improving {skill} through a course or project.")

    return recommendations