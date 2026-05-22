from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.8)

def content_agent(strategy, research, platform, brand):
    prompt = f"""
    You are a social media content creator.
    
    Brand: {brand}
    Platform: {platform}
    
    Strategy: {strategy}
    Research & Trends: {research}
    
    Create 3 ready-to-post content pieces for {platform}:
    
    For each post provide:
    1. Caption (platform appropriate length)
    2. 5 hashtags
    3. Call to action
    4. Best time to post
    
    Make it engaging and professional.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content