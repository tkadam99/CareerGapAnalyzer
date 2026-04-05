from pathlib import Path
import pandas as pd
import pdfplumber


def load_text_file(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def load_csv_file(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)


def load_jobs_csv(path):
    df = load_csv_file(path)

    required_columns = {"job_title", "company", "description"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns in jobs CSV: {missing_columns}")

    return df


def extract_text_from_pdf(pdf_file):
    extracted_text = []

    # CHANGE: reset file pointer before reading PDF
    # This helps ensure the uploaded PDF is read from the beginning every time.
    pdf_file.seek(0)

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text.append(page_text)

    return "\n".join(extracted_text)


def load_resume_file(uploaded_file):
    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        # CHANGE: reset file pointer before reading TXT
        uploaded_file.seek(0)
        return uploaded_file.read().decode("utf-8")

    if file_name.endswith(".pdf"):
        # CHANGE: PDF handling goes through the safer parser above
        uploaded_file.seek(0)
        return extract_text_from_pdf(uploaded_file)

    raise ValueError("Unsupported file type. Please upload a TXT or PDF resume.")