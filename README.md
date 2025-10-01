# Storytelling Agent (YouTube Automation)

## 🚀 Setup Guide

### 1. Upload to GitHub
- इस ZIP को extract करके GitHub पर नया repo बनाइए।
- Repo → Settings → Secrets and variables → Actions में दो secrets डालिए:
  - `OPENAI_API_KEY` → आपकी OpenAI key
  - `CLIENT_SECRET_JSON` → पूरा JSON text (Google OAuth credentials)

### 2. Run GitHub Actions
- Actions tab → "Build Windows EXE" workflow → Run workflow.
- Build complete होने के बाद Artifacts से `.exe` डाउनलोड कर लीजिए।

### 3. Run EXE on Windows
- Python install करने की ज़रूरत नहीं है।
- पहली बार चलाते समय Google OAuth खुलेगा ताकि YouTube upload authorize हो सके।

---

## ⚠️ Important Notes
- अपनी API keys को कभी भी कोड में hardcode मत करें।
- हमेशा GitHub Secrets का इस्तेमाल करें।
- EXE का size बड़ा (~150MB) होगा क्योंकि इसमें Python bundle होता है।
