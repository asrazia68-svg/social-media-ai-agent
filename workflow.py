from agents.strategy_agent import strategy_agent
from agents.research_agent import research_agent
from agents.content_agent import content_agent
from agents.review_agent import review_agent

def run_workflow(brand, goal, audience, platforms):
    
    print("🔵 Step 1: Strategy Agent chal raha hai...")
    strategy = strategy_agent(brand, goal, audience, platforms)
    print("✅ Strategy ready!")
    
    print("🔵 Step 2: Research Agent chal raha hai...")
    research = research_agent(brand, platforms)
    print("✅ Research ready!")
    
    print("🔵 Step 3: Content Agent chal raha hai...")
    all_posts = []
    for platform in platforms:
        content = content_agent(strategy, research, platform, brand)
        all_posts.append({
            "platform": platform,
            "content": content
        })
    print("✅ Content ready!")
    
    print("🔵 Step 4: Review Agent chal raha hai...")
    reviewed_posts = []
    for post in all_posts:
        review = review_agent(post["content"], brand, post["platform"])
        reviewed_posts.append({
            "platform": post["platform"],
            "content": post["content"],
            "review": review
        })
    print("✅ Review ready!")
    
    return {
        "strategy": strategy,
        "research": research,
        "posts": reviewed_posts
    }