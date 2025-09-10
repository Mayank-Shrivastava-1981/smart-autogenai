import streamlit as st
from langchain_core.runnables import RunnableConfig
from main import app  # Import your LangGraph workflow (your provided code saved as main.py)

# ------------------------
# Streamlit UI
# ------------------------
st.set_page_config(page_title="Automation Code Generator", layout="wide")

st.title("🚀 GenAI Test Automation Code Generator")

# Input fields
url = st.text_input("🔗 Enter URL", placeholder="https://example.com")
selectedLanguage = st.selectbox("🖥️ Select Language", ["Java", "Python", "JavaScript","C#"])
selectedTool = st.selectbox("⚙️ Select Framework/Tool", ["Selenium", "Playwright"," Cypress","Puppeteer","TestCafe","WebDriverIO","Robot Framework","Katalon Studio"])
testCase = st.text_input("📝 Test Case Name", placeholder="Login with valid credentials")
testData = st.text_area("📂 Test Data", placeholder="username=admin, password=admin123")
testSteps = st.text_area("📜 Test Steps", placeholder="Enter username, Enter password, Click login")

# Run button
if st.button("⚡ Generate Code"):
    with st.spinner("Generating automation code..."):
        inputs = {
            "url": url,
            "selectedLanguage": selectedLanguage,
            "selectedTool": selectedTool,
            "testCase": testCase,
            "testData": testData,
            "testSteps": testSteps
        }
        result = app.invoke(inputs, config=RunnableConfig())

        if "generated_code" in result:
            st.success("✅ Code generated successfully!")
            st.code(result["generated_code"], language="java" if selectedLanguage=="Java" else selectedLanguage.lower())
        else:
            st.error("❌ Failed to generate code. Try again.")
