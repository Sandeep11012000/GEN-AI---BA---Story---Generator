# GEN-AI---BA---Story---Generator
A lightweight web application where a user uploads a text snippet or document of a business requirement, and a Large Language Model (LLM) instantly generates structured User Stories, Acceptance Criteria (in Given-When-Then / Gherkin format), and a draft functional testing plan.

## 📺 Project Walkthrough & Technical Demo

*A complete system overview and live generation walkthrough demonstrating dynamic prompt engineering and model execution.*
https://github.com/user-attachments/assets/45be5f73-10a8-4be1-b162-a6f95375ff8c

## 🎯 Executive Summary & Problem Statement
In traditional software development, translating vague stakeholder feedback, emails, or meeting notes into structured, developer-ready user stories is a highly manual, error-prone bottleneck. 

This project bridges that operational gap by combining a **Python (Streamlit)** frontend UI layer with the **Google Gemini 3.5 Flash** large language model. By injecting highly engineered system prompts and enforcing low-temperature inference, this tool programmatically guarantees standardized backlog formatting in seconds.

### 🌟 Key Product Capabilities:
* **Dynamic Framework Adaptability:** Switches instantly between standard Agile User Stories (`As a... I want to... So that...`) and Outcome-driven Job Stories (`When... I want to... So I can...`).
* **BDD Automation:** Generates syntax-perfect Gherkin acceptance criteria (`Given-When-Then`) ready for automated testing suites (Cucumber/Behave).
* **Deterministic Formatting:** Restricts LLM behavioral randomness through precise context parameterization.

💡 Strategic Value as a Business Analyst - This implementation proves more than just basic coding literacy. It showcases a modern Business Analyst's ability to:

* Leverage Frontier AI APIs: Transitioning the role from manual requirements drafting to programmatic prompt-engineering orchestration.
* Design Modular Software Systems: Utilizing isolated client configurations, session management variables, and responsive split-column visual layouts.
* Enforce Structural Governance: Restricting generative flexibility through deterministic variables to produce standardized business data packages.

UI Screen:

<img width="1897" height="797" alt="Image_4" src="https://github.com/user-attachments/assets/4230e9ee-d837-4fdf-9882-8dd433327475" />


