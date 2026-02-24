import streamlit as st
from utils.news_api_check import check_live_news
from utils.fact_check import fact_check_news
from utils.ai_check import ai_fake_check
from utils.claim_filter import has_fake_claim_pattern

st.title("📰 Fake News Detection System")

news_text = st.text_area("Paste News Text (From App / Channel / Website)")

if st.button("Check News"):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter news text")
    else:
        live_result = check_live_news(news_text)
        fact_result = fact_check_news(news_text)
        ai_label, ai_score = ai_fake_check(news_text)
        fake_claim = has_fake_claim_pattern(news_text)

        st.subheader("🔍 Analysis Result")

        # 🚨 STRONG FAKE CLAIM RULE
        if fake_claim and not fact_result:
            st.error("❌ MOST LIKELY FAKE NEWS (Unverified mass-benefit claim)")

        # 🤖 AI FAIL-SAFE
        elif ai_label in ["ai_busy", "ai_loading", "ai_error", "ai_exception"]:
            if live_result and not fake_claim:
                st.success("✅ MOST LIKELY TRUE NEWS (Live source found)")
            elif not live_result:
                st.error("❌ MOST LIKELY FAKE NEWS (No live source found)")
            else:
                st.warning("⚠️ UNCERTAIN — Needs manual verification")

        # 🤖 AI AVAILABLE
        elif ai_label == "true news":
            st.success(f"✅ TRUE NEWS ({ai_score*100:.2f}% confidence)")
        elif ai_label == "fake news":
            st.error(f"❌ FAKE NEWS ({ai_score*100:.2f}% confidence)")
        else:
            st.warning("⚠️ UNCERTAIN — Manual verification needed")

        with st.expander("🛠 Debug Details"):
            st.write("Live News Found:", live_result)
            st.write("Fact Check Found:", fact_result)
            st.write("Fake Claim Pattern:", fake_claim)
            st.write("AI Status:", ai_label)
            st.write("AI Confidence:", ai_score)