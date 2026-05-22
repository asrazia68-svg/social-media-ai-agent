import streamlit as st
from workflow import run_workflow

st.set_page_config(
    page_title="AI Social Media Agent",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

.stApp {
    background: #0a0a0f;
    background-image: 
        radial-gradient(ellipse at 20% 50%, rgba(0, 255, 163, 0.05) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 163, 255, 0.05) 0%, transparent 50%);
    font-family: 'Rajdhani', sans-serif;
}

.hero {
    text-align: center;
    padding: 60px 20px 40px;
}

.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: 3.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00ffa3, #00a3ff, #7b2fff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero-sub {
    color: #4a5568;
    font-size: 1.1rem;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.neon-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, #00ffa3, #00a3ff, transparent);
    margin: 30px auto;
    max-width: 600px;
}

.card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(0, 255, 163, 0.15);
    border-radius: 16px;
    padding: 32px;
    margin-bottom: 24px;
}

.section-label {
    font-family: 'Orbitron', monospace;
    font-size: 0.65rem;
    letter-spacing: 4px;
    color: #00ffa3;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(0,255,163,0.3), transparent);
}

/* INPUT TEXT WHITE */
.stTextInput > div > div > input {
    background: #ffffff !important;
    border: 1px solid rgba(0, 255, 163, 0.25) !important;
    border-radius: 10px !important;
    color: #000000 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1.05rem !important;
    padding: 12px 16px !important;
}

.stTextInput > div > div > input::placeholder {
    color: #555 !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00ffa3 !important;
    box-shadow: 0 0 20px rgba(0, 255, 163, 0.1) !important;
    color: #000000 !important;
}

/* SELECTBOX WHITE TEXT */
.stSelectbox > div > div {
    background: #ffffff !important;
    border: 1px solid rgba(0, 255, 163, 0.25) !important;
    border-radius: 10px !important;
    color: #000000 !important;
}

.stSelectbox > div > div > div {
    color: #000000 !important;
}

/* MULTISELECT WHITE TEXT */
.stMultiSelect > div > div {
    background: #ffffff !important;
    border: 1px solid rgba(0, 255, 163, 0.25) !important;
    border-radius: 10px !important;
    color: #000000 !important;
}

.stMultiSelect span {
    color: #000000 !important;
}

/* LABELS */
label, .stSelectbox label, .stTextInput label, .stMultiSelect label {
    color: #00ffa3 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* BUTTON */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #00ffa3, #00a3ff) !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 16px 32px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    margin-top: 10px !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 40px rgba(0, 255, 163, 0.3) !important;
}

/* RESULT CARDS */
.result-card {
    background: rgba(0, 255, 163, 0.03);
    border: 1px solid rgba(0, 255, 163, 0.1);
    border-left: 3px solid #00ffa3;
    border-radius: 12px;
    padding: 24px;
    margin: 16px 0;
    color: #e2e8f0;
    font-family: 'Rajdhani', sans-serif;
    font-size: 1rem;
    line-height: 1.8;
    white-space: pre-wrap;
}

.platform-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(0,255,163,0.15), rgba(0,163,255,0.15));
    border: 1px solid rgba(0,255,163,0.3);
    border-radius: 20px;
    padding: 4px 16px;
    font-family: 'Orbitron', monospace;
    font-size: 0.7rem;
    letter-spacing: 2px;
    color: #00ffa3;
    margin-bottom: 12px;
}

.review-card {
    background: rgba(0, 163, 255, 0.03);
    border: 1px solid rgba(0, 163, 255, 0.1);
    border-left: 3px solid #00a3ff;
    border-radius: 12px;
    padding: 20px;
    margin-top: 12px;
    color: #a0aec0;
    font-size: 0.95rem;
    line-height: 1.7;
    white-space: pre-wrap;
}

h2, h3 {
    font-family: 'Orbitron', monospace !important;
    color: #e2e8f0 !important;
    letter-spacing: 2px !important;
}
</style>

<div class="hero">
    <div class="hero-title">⚡ AI Social Media Agent</div>
    <div class="hero-sub">Multi-Agent Content Generation System</div>
</div>
<div class="neon-line"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-label">▸ Brand Configuration</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    brand = st.text_input("Brand Name", placeholder="e.g. Cyber Security Academy")
    audience = st.text_input("Target Audience", placeholder="e.g. Students and Professionals")
with col2:
    goal = st.selectbox("Campaign Goal", ["Brand Awareness", "Generate Leads", "Sales", "Engagement"])
    platforms = st.multiselect("Target Platforms", ["Instagram", "LinkedIn", "Twitter", "Facebook", "TikTok"], default=["Instagram", "LinkedIn"])

st.markdown('</div>', unsafe_allow_html=True)

if st.button("⚡ GENERATE CONTENT"):
    if not platforms:
        st.error("Kam az kam ek platform select karo!")
    elif not brand:
        st.error("Brand name zaroor likho!")
    else:
        with st.spinner("AI Agents kaam kar rahe hain..."):
            result = run_workflow(brand, goal, audience, platforms)

        st.success("✅ Content Generation Complete!")
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="section-label">▸ Strategy Output</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-card">{result["strategy"]}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="section-label">▸ Market Research</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-card">{result["research"]}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="section-label">▸ Generated Posts</div>', unsafe_allow_html=True)
        for post in result["posts"]:
            st.markdown(f'<div class="platform-badge">📱 {post["platform"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-card">{post["content"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="review-card">🔍 <strong>AI Review:</strong><br>{post["review"]}</div>', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)