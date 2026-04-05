import streamlit as st

st.title("📄 Resume Analyzer")

# Upload file
uploaded_file = st.file_uploader("Upload Resume", type=["txt"])

# Always show text box
resume_text = st.text_area("Enter your Resume text")

# If file uploaded → override text
if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8")

skills = ["python", "java", "sql", "machine learning", "data analysis"]

if st.button("Analyze Resume"):

    if resume_text.strip() == "":
        st.warning("⚠️ Please enter your resume text")

    else:
        resume_text = resume_text.lower()

        st.subheader("🔍 Analysis Result:")

        found_skills = []

        for skill in skills:
            if skill in resume_text:
                found_skills.append(skill)

        if found_skills:
            st.success("✅ Skills found: " + ", ".join(found_skills))
        else:
            st.error("❌ No matching skills found")

        # Score
        score = (len(found_skills) / len(skills)) * 100
        st.subheader(f"⭐ Resume Score: {int(score)}%")
        st.progress(int(score))

        # Suggestions
        st.subheader("💡 Suggestions:")
        for skill in skills:
            if skill not in resume_text:
                st.write(f"- Add {skill}")