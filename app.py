import streamlit as st
from google import genai
from google.genai import types

# 1. Page Configuration
st.set_page_config(
    page_title="AI Requirements Engineer Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar Configuration
with st.sidebar:
    st.title("⚙️ System Config")
    st.subheader("Model Settings")
    
    # Live API Key Box
    gemini_key = st.text_input("Enter Gemini API Key", type="password", 
                               help="Get a free API key from Google AI Studio.")
    
    st.markdown("---")
    st.subheader("Framework Parameters")
    story_format = st.selectbox("User Story Format", ["Standard (As a... I want to...)", "Job Stories (When... I want to... So I can...)"])
    criteria_format = st.selectbox("Acceptance Criteria", ["Gherkin (Given-When-Then)", "Verification Checklist"])

# 3. Main Header Metrics Dashboard
st.title("🤖 AI-Driven BRD to Agile Story Converter")
st.caption("A GenAI Portfolio Project demonstrating Automated Requirements Elaboration & Live LLM Integration.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Connected LLM Engine", value="Gemini 2.5 Flash" if gemini_key else "Not Connected")
with col2:
    st.metric(label="API Status", value="Live Dynamic" if gemini_key else "Demo Mode Only")
with col3:
    st.metric(label="BA Process Efficiency", value="4x Faster", delta="300%")

st.markdown("---")

# 4. Input / Output Split Layout
left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.subheader("📋 Raw Business Requirement Input")
    
    sample_text = (
        "We need to add a password reset feature because users keep locking themselves out. "
        "It should send them an email with a link that expires in 24 hours."
    )
    
    raw_requirement = st.text_area(
        label="BRD Content Box",
        value=sample_text, 
        height=280,
        label_visibility="collapsed"
    )
    
    generate_btn = st.button("🚀 Analyze & Generate Agile Artifacts", use_container_width=True, type="primary")

with right_col:
    st.subheader("🎯 Generated Product Backlog Items")
    
    if generate_btn:
        if not gemini_key:
            st.error("⚠️ Please enter a valid Gemini API Key in the left sidebar configuration to run this dynamically.")
        else:
            with st.spinner("GenAI Processing Engine executing prompt matrices via Gemini..."):
                try:
                    # Initialize the real Gemini Client
                    client = genai.Client(api_key=gemini_key)
                    
                    # Core Prompt Engineering Definition
                    system_prompt = (
                        f"You are a Principal Technical Product Owner. Process the user's raw requirement into "
                        f"structured Agile requirements. You must output exactly two explicit parts split clearly by a '---' line.\n\n"
                        f"Part 1: Provide 1-2 User Stories structured exactly using the format: '{story_format}'. "
                        f"Format each story cleanly inside individual markdown block titles.\n\n"
                        f"Part 2: Provide clear Acceptance Criteria formatted explicitly as '{criteria_format}' format."
                    )
                    
                    # Run the dynamic call to the LLM
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=raw_requirement,
                        config=types.GenerateContentConfig(
                            system_instruction=system_prompt,
                            temperature=0.2
                        )
                    )
                    
                    # Parse out the response parts visually 
                    output_text = response.text
                    
                    tab1, tab2 = st.tabs(["📝 User Stories & Acceptance Criteria", "🛠️ Prompt Analytics"])
                    
                    with tab1:
                        st.markdown(output_text)
                        
                    with tab2:
                        st.info("💡 **Senior BA Portfolio Insight:** Below is the exact system configuration package injected into Gemini's generation token stream.")
                        st.code(system_prompt, language="text")
                        
                except Exception as e:
                    st.error(f"API Execution Error: {str(e)}")
    else:
        st.info("👈 Enter your key and click 'Analyze' on the left to process your custom requirements live.")
