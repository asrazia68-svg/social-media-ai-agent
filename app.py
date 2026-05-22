import streamlit as st
from workflow import run_workflow

st.set_page_config(page_title="AI Social Media Agent", page_icon="🤖")
st.title("🤖 AI Social Media Agent")
st.subheader("Apna brand info do — AI posts banayega!")

brand = st.text_input("Brand Name", "AI Academy")
goal = st.selectbox("Goal", ["Brand Awareness", "Generate Leads", "Sales", "Engagement"])
audience = st.text_input("Target Audience", "Students and Professionals")
platforms = st.multiselect("Platforms", ["Instagram", "LinkedIn", "Twitter", "Facebook"], default=["Instagram"])

if st.button("🚀 Posts Generate Karo"):
    with st.spinner("AI agents kaam kar rahe hain... thoda wait karo ⏳"):
        result = run_workflow(brand, goal, audience, platforms)
    
    st.success("✅ Done!")
    
    st.subheader("📋 Strategy")
    st.write(result["strategy"])
    
    st.subheader("🔍 Research")
    st.write(result["research"])
    
    st.subheader("📱 Generated Posts")
    for post in result["posts"]:
        st.markdown(f"### {post['platform']}")
        st.write(post["content"])
        st.markdown("**✅ Review:**")
        st.write(post["review"])
        st.divider()