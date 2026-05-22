from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

def research_agent(brand, platforms):
    prompt = f"""
    You are a social media research expert.
    
    Brand: {brand}
    Platforms: {', '.join(platforms)}
    
    Research and provide:
    1. 5 trending topics in this industry
    2. 10 best hashtags to use
    3. Best posting times for each platform
    4. Content ideas from competitors
    
    Keep it practical and specific.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content