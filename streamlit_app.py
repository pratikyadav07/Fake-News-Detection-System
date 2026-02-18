import streamlit as st
from src.predict import predict_news

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("📰 Fake News Detection System")
st.markdown(
    """
    This system uses:
    - 🤖 Machine Learning
    - 🧠 Entity Extraction
    - 🔎 Rule-based Fact Verification
    
    It classifies news into:
    **REAL / FAKE / POTENTIALLY MISLEADING**
    """
)

# ---------------- INPUT ----------------
news_text = st.text_area("Enter News Text Below", height=200)

# ---------------- BUTTON ----------------
if st.button("Analyze News"):

    if news_text.strip() == "":
        st.warning("⚠️ Please enter some news text")
    else:
        with st.spinner("Analyzing..."):
            result = predict_news(news_text)

        st.divider()
        st.subheader("🔍 Analysis Result")

        label = result["label"]
        confidence = round(result["confidence"] * 100, 2)

        # ----------- RESULT DISPLAY -----------
        if label == "FAKE":
            st.error(f"❌ FAKE NEWS\n\nConfidence: {confidence}%")

        elif label == "REAL":
            st.success(f"✅ REAL NEWS\n\nConfidence: {confidence}%")

        else:
            st.warning(f"⚠️ POTENTIALLY MISLEADING\n\nConfidence: {confidence}%")

        # ----------- REASONS -----------
        if result.get("reason"):
            st.markdown("### 🧾 Reasoning")
            for r in result["reason"]:
                st.write(f"- {r}")

        # ----------- ENTITIES -----------
        with st.expander("🔎 Extracted Entities"):
            st.json(result.get("entities", {}))

        st.divider()
        st.caption("Built with ML + NLP + Rule-based Fact Checking")
