from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

def strategy_agent(brand, goal, audience, platforms):
    prompt = f"""
    You are a social media strategy expert.
    
    Brand: {brand}
    Goal: {goal}
    Target Audience: {audience}
    Platforms: {', '.join(platforms)}
    
    Create a content strategy with:
    1. 3 content pillars (topics)
    2. Tone and style
    3. Posting tips
    
    Keep it concise and practical.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content