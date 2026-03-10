# 📰 Fake News Detection System

A **multi-layer Fake News Detection System** that verifies news using live news APIs, fact-check APIs and AI models.  
The system analyzes a news statement and determines whether it is **True, Fake, or Uncertain**.

The project is built using **Python, Streamlit, APIs, and AI-based text analysis**.

---

## 🚀 Features

- Detects fake news using multiple verification layers
- Uses **Live News API** to check if news exists in trusted sources
- Uses **Google Fact Check API** for verified claims
- Uses **AI model (HuggingFace)** for text classification
- Includes **rule-based claim detection** for viral fake schemes
- Provides **confidence score and debugging information**
- Interactive **Streamlit web interface**

---

## 🧠 How It Works

The system follows a multi-step verification process:

1. **Live News Verification**
   - Checks whether the news exists in real news sources using NewsAPI.

2. **Fact Check Verification**
   - Searches Google's Fact Check database for verified claims.

3. **AI-Based Analysis**
   - Uses a HuggingFace NLP model to classify the news text.

4. **Claim Pattern Detection**
   - Detects suspicious patterns such as viral money schemes.

5. **Final Decision**
   - Combines all results to determine if the news is:
     - ✅ True News
     - ❌ Fake News
     - ⚠️ Uncertain

---

## 🛠 Technologies Used

- Python
- Streamlit
- NewsAPI
- Google Fact Check API
- HuggingFace API
- Natural Language Processing (NLP)

---

## 📂 Project Structure
