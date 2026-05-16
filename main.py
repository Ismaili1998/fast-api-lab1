from fastapi import FastAPI
import requests
from .crud import insert_posts
from .init_db import init_db
app = FastAPI()

REDDIT_URL = "https://www.reddit.com/r/Artificial/hot.json"

AI_TOOLS = [
    "ChatGPT", "GPT-4", "Midjourney", "Claude", "Gemini",
    "Perplexity", "Copilot", "Llama", "Mistral", "Grok"
]


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Trending AI Tools API"}

@app.get("/trending-ai-tools")
def get_trending_ai_tools():
    headers = {
		"User-Agent": "Mozilla/5.0 (compatible; TrendingAIToolsBot/1.0)"
	}

    try:
        response = requests.get(REDDIT_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

    results = []

    # only 10 posts, sorted by popularity score (highest first)
    posts = sorted(data["data"]["children"], key=lambda x: x["data"]["score"], reverse=True)[:10]

    for post in posts:
        post_data = post["data"]
        title = post_data["title"]

        # detect tool
        detected_tool = None
        for tool in AI_TOOLS:
            if tool.lower() in title.lower():
                detected_tool = tool
                break

        insert_posts(results)

        results.append({
            "title": title,
            "url": "https://reddit.com" + post_data["permalink"],
            "score": post_data["score"],
            "tool": detected_tool
        })

    return {
        "count": len(results),
        "posts": results
    }