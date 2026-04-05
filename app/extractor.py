import re
import pandas as pd
from app.preprocessor import clean_text


def load_skill_dictionary(skills_csv_path):
    df = pd.read_csv(skills_csv_path)
    skill_map = {}

    for _, row in df.iterrows():
        canonical = row["skill_name"].strip()
        aliases = [alias.strip().lower() for alias in str(row["aliases"]).split(",")]

        # include canonical name itself
        aliases.append(canonical.lower())

        for alias in aliases:
            skill_map[alias] = canonical

    return skill_map


def extract_skills(text, skill_map):
    cleaned_text = clean_text(text)
    found_skills = set()

    # longer aliases first helps phrase matching
    sorted_aliases = sorted(skill_map.keys(), key=len, reverse=True)

    for alias in sorted_aliases:
        canonical = skill_map[alias]

        # whole phrase / word style matching
        pattern = r"(?<!\w)" + re.escape(alias) + r"(?!\w)"
        if re.search(pattern, cleaned_text):
            found_skills.add(canonical)

    return sorted(found_skills)