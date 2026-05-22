from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)

def review_agent(content, brand, platform):
    prompt = f"""
    You are a social media content reviewer.
    
    Brand: {brand}
    Platform: {platform}
    
    Review this content:
    {content}
    
    Check and provide:
    1. Grammar and spelling errors
    2. Brand consistency (professional tone)
    3. Platform policy compliance
    4. Engagement potential (rate 1-10)
    5. Final verdict: APPROVED or NEEDS CHANGES
    6. Suggestions for improvement
    
    Be specific and helpful.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content