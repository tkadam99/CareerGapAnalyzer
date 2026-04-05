import pandas as pd
import streamlit as st
from app.main import analyze_texts, analyze_resume_vs_market
from app.config import (
    SAMPLE_RESUME_PATH,
    SAMPLE_JOB_DESCRIPTION_PATH,
    SAMPLE_JOBS_CSV_PATH,
)
from app.parser import load_text_file, load_jobs_csv, load_resume_file


def format_skill_list(skills, prefix=""):
    if not skills:
        return "None"
    return ", ".join([f"{prefix}{skill}" for skill in skills])


st.set_page_config(page_title="Career Gap Analyzer", layout="wide")

st.title("AI-Powered Career Gap Analyzer")
st.write("Analyze your resume against a job description or the broader job market.")

# Load default data
default_resume = load_text_file(SAMPLE_RESUME_PATH)
default_job = load_text_file(SAMPLE_JOB_DESCRIPTION_PATH)
default_jobs_df = load_jobs_csv(SAMPLE_JOBS_CSV_PATH)

mode = st.radio(
    "Choose Analysis Mode",
    ["Single Job Analysis", "Market Analysis"]
)

# Resume Input
st.subheader("Resume Input")

uploaded_resume = st.file_uploader(
    "Upload Resume (TXT or PDF)",
    type=["txt", "pdf"]
)

if uploaded_resume is not None:
    try:
        resume_text = load_resume_file(uploaded_resume)
        st.success("Resume uploaded successfully.")
    except Exception as e:
        st.error(f"Error reading resume file: {e}")
        resume_text = ""
else:
    resume_text = st.text_area(
        "Or Paste Resume Text",
        value=default_resume,
        height=220
    )

# ================= SINGLE JOB =================
if mode == "Single Job Analysis":
    job_text = st.text_area(
        "Paste Job Description",
        value=default_job,
        height=180
    )

    if st.button("Analyze Resume vs Job"):
        if not resume_text.strip():
            st.error("Please upload or paste a resume before analysis.")
        elif not job_text.strip():
            st.error("Please provide a job description.")
        else:
            results = analyze_texts(resume_text, job_text)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔍 Extracted Skills")

                st.write("**Resume Skills:**")
                st.markdown(format_skill_list(results["resume_skills"]))

                st.write("**Job Skills:**")
                st.markdown(format_skill_list(results["job_skills"]))

                st.subheader("⚖️ Skill Comparison")

                st.write("**Matched Skills:**")
                st.markdown(format_skill_list(results["matched_skills"], "✅ "))

                st.write("**Missing Skills:**")
                st.markdown(format_skill_list(results["missing_skills"], "❌ "))

                st.write("**Extra Skills:**")
                st.markdown(format_skill_list(results["extra_skills"], "➕ "))

            with col2:
                st.subheader("📊 Fit Assessment")

                st.metric("Fit Score", f"{results['fit_score']}%")
                st.progress(results["fit_score"] / 100)

                st.write("**Category:**")
                if results["fit_category"] == "Strong Match":
                    st.success(results["fit_category"])
                elif results["fit_category"] == "Moderate Match":
                    st.warning(results["fit_category"])
                else:
                    st.error(results["fit_category"])

                st.subheader("🧠 Recommendations")
                for rec in results["recommendations"]:
                    st.success(rec)

                st.subheader("💡 Insights")
                if results["missing_skills"]:
                    st.warning(
                        f"You are missing {len(results['missing_skills'])} key skills. "
                        f"Focus on: {', '.join(results['missing_skills'][:2])}"
                    )
                else:
                    st.success("Your profile strongly matches the job requirements.")

            st.divider()

            st.subheader("📈 Skill Match Overview")
            chart_data = pd.DataFrame({
                "Category": ["Matched", "Missing", "Extra"],
                "Count": [
                    len(results["matched_skills"]),
                    len(results["missing_skills"]),
                    len(results["extra_skills"]),
                ],
            })
            st.bar_chart(chart_data.set_index("Category"))

# ================= MARKET ANALYSIS =================
elif mode == "Market Analysis":
    st.info("Market analysis uses the built-in dataset (sample_jobs.csv).")

    if st.button("Analyze Resume vs Market"):
        if not resume_text.strip():
            st.error("Please upload or paste a resume.")
        else:
            results = analyze_resume_vs_market(resume_text, default_jobs_df)

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔍 Extracted Skills")

                st.write("**Resume Skills:**")
                st.markdown(format_skill_list(results["resume_skills"]))

                st.write("**Market Skills:**")
                st.markdown(format_skill_list(results["market_skills"]))

                st.subheader("⚖️ Skill Comparison")

                st.write("**Matched Skills:**")
                st.markdown(format_skill_list(results["matched_skills"], "✅ "))

                st.write("**Missing Skills:**")
                st.markdown(format_skill_list(results["missing_skills"], "❌ "))

                st.write("**Top Missing Skills:**")
                st.markdown(format_skill_list(results["top_missing_skills"], "⚠️ "))

                st.write("**Extra Skills:**")
                st.markdown(format_skill_list(results["extra_skills"], "➕ "))

            with col2:
                st.subheader("📊 Fit Assessment")

                st.metric("Simple Fit Score", f"{results['fit_score']}%")
                st.progress(results["fit_score"] / 100)

                st.metric("Weighted Fit Score", f"{results['weighted_fit_score']}%")
                st.progress(results["weighted_fit_score"] / 100)

                st.write("**Category:**")
                if results["fit_category"] == "Strong Match":
                    st.success(results["fit_category"])
                elif results["fit_category"] == "Moderate Match":
                    st.warning(results["fit_category"])
                else:
                    st.error(results["fit_category"])

                st.subheader("🏆 Top Market Skills")
                for skill, freq in list(results["market_skill_frequency"].items())[:5]:
                    st.write(f"**{skill}** → {freq}")

                st.subheader("🧠 Recommendations")
                for rec in results["recommendations"]:
                    st.success(rec)

                st.subheader("💡 Insights")
                if results["missing_skills"]:
                    st.warning(
                        f"You are missing {len(results['missing_skills'])} important market skills. "
                        f"Top gaps: {', '.join(results['top_missing_skills'][:2])}"
                    )
                else:
                    st.success("Your profile strongly matches market demand.")

            st.divider()

            st.subheader("📈 Market Skill Match Overview")
            market_match_data = pd.DataFrame({
                "Category": ["Matched", "Missing", "Extra"],
                "Count": [
                    len(results["matched_skills"]),
                    len(results["missing_skills"]),
                    len(results["extra_skills"]),
                ],
            })
            st.bar_chart(market_match_data.set_index("Category"))

            st.subheader("📊 Market Skill Demand")
            freq_df = pd.DataFrame(
                list(results["market_skill_frequency"].items()),
                columns=["Skill", "Frequency"]
            )
            st.bar_chart(freq_df.set_index("Skill"))