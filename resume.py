import streamlit as st
st.title("Resume Analyzer")
st.write("Paste your resume below:")
resume_text = st.text_area("Enter your Resume text")
skills = ["Python","Machine learning","data analysis","Java"]
if resume_text:
    resume_text = resume_text.lower()
    st.subheader("Analysis Result:")
    found_skills = []
    for skill in skills:
        if skill in resume_text:
            found_skills.append(skill)
    if found_skills:
        st.write("Skill found:",",".join(found_skills))
    else:
        st.write("No matching skills found")
    st.subheader("Suggestions:")
    if "python" not in resume_text:
        st.write("-Add python skills")
    if "Machine learning" not in resume_text:
        st.write("-Add Machine Learning projects")

