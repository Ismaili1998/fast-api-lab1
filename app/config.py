"""Application Configuration"""

import os
from dotenv import load_dotenv

load_dotenv()

# Database Configuration
DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "db"),
    "user": os.getenv("DB_USER", "admin"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "host": os.getenv("DB_HOST", "postgres-container"),
    "port": int(os.getenv("DB_PORT", 5432))
}

# API Configuration
REDDIT_URL = "https://www.reddit.com/r/Artificial/hot.json"

AI_TOOLS = [
    "ChatGPT", "GPT-4", "Midjourney", "Claude", "Gemini",
    "Perplexity", "Copilot", "Llama", "Mistral", "Grok"
]

USER_AGENT = "Mozilla/5.0 (compatible; TrendingAIToolsBot/1.0)"
