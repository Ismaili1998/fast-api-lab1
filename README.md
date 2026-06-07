# Trending AI Tools API

A FastAPI application that fetches and tracks trending AI tools mentioned on Reddit.

## Project Structure

```
fast-api/
├── app/                 # Main application package
│   ├── __init__.py
│   ├── main.py         # FastAPI app & routes
│   ├── config.py       # Configuration settings
│   ├── db.py           # Database connection
│   └── crud.py         # Database operations
├── scripts/
│   └── init_db.py      # Database initialization
├── tests/              # Test directory
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features

- Fetch trending AI tools from Reddit's r/Artificial subreddit
- Detect AI tool mentions in post titles (ChatGPT, Claude, Gemini, etc.)
- Store trends in PostgreSQL database
- RESTful API endpoints for accessing trending data

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL database
- Docker (optional)

### Installation

1. Clone the repository
2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- `GET /` - Health check
- `GET /trending-ai-tools` - Fetch trending AI tools from Reddit

## Docker

Build and run with Docker:

```bash
docker build -t trending-ai-api .
docker run -p 8000:8000 --env-file .env trending-ai-api
```

## Database

The application automatically initializes the required database table on startup. The schema includes:

- `id` - Primary key
- `title` - Post title from Reddit
- `url` - Post URL
- `score` - Upvote score
- `tool` - Detected AI tool name
- `created_at` - Timestamp

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Add tests in the `tests/` directory
4. Submit a pull request

## License

MIT
