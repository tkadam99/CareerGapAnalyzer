from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

SAMPLE_RESUME_PATH = DATA_DIR / "sample_resume.txt"
SAMPLE_JOB_DESCRIPTION_PATH = DATA_DIR / "sample_job_description.txt"
SKILLS_MASTER_PATH = DATA_DIR / "skills_master.csv"
LEARNING_RESOURCES_PATH = DATA_DIR / "learning_resources.csv"
SAMPLE_JOBS_CSV_PATH = DATA_DIR / "sample_jobs.csv"