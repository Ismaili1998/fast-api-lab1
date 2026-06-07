"""Main FastAPI Application"""

import requests
from fastapi import FastAPI, HTTPException
from app.config import REDDIT_URL, AI_TOOLS, USER_AGENT
from app.crud import insert_posts
from scripts.init_db import init_db

app = FastAPI(
    title="Trending AI Tools API",
    description="API to fetch and track trending AI tools from Reddit",
    version="1.0.0"
)


@app.on_event("startup")
def startup():
    """Initialize database on startup"""
    init_db()


@app.get("/")
def root():
    """Root endpoint"""
    return {"message": "Trending AI Tools API"}


@app.get("/trending-ai-tools")
def get_trending_ai_tools():
    """Fetch trending AI tools from Reddit and store in database"""
    headers = {"User-Agent": USER_AGENT}

    try:
        response = requests.get(REDDIT_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    results = []
    posts = sorted(data["data"]["children"], key=lambda x: x["data"]["score"], reverse=True)[:10]

    for post in posts:
        post_data = post["data"]
        title = post_data["title"]

        detected_tool = None
        for tool in AI_TOOLS:
            if tool.lower() in title.lower():
                detected_tool = tool
                break

        results.append({
            "title": title,
            "url": post_data["url"],
            "score": post_data["score"],
            "tool": detected_tool
        })

    insert_posts(results)
    return {"trending_tools": results}
