# FastAPI with PostgreSQL - Docker Setup Guide

## Prerequisites

- Docker installed and running

---

## Step 1: Build the FastAPI Image

Create a Docker image for the FastAPI application:

```bash
docker build -t fast-api-image .
```

Verify the image was created:

```bash
docker images
```

---

## Step 2: Pull PostgreSQL Image

Download the latest PostgreSQL image from Docker Hub:

```bash
docker pull postgres
```

---

## Step 3: Create a Docker Network

Create a custom network to connect both containers:

```bash
docker network create fast-api-network
```

---

## Step 4: Create PostgreSQL Container

Run PostgreSQL in a container on the network:

```bash
docker run -d \
  --name postgres-container \
  --network fast-api-network \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=db \
  -p 5432:5432 \
  postgres
```

**Container details:**

- Name: `postgres-container`
- User: `admin`
- Password: `root`
- Database: `db`
- Port: `5432`

---

## Step 5: Create FastAPI Container

Run the FastAPI application in a container on the same network:

```bash
docker run -d \
  --name fast-api-container \
  --network fast-api-network \
  -p 8000:8000 \
  fast-api-image
```

**Container details:**

- Name: `fast-api-container`
- API Port: `8000` (accessible at `http://localhost:8000`)

---

## Step 6: Verify the Setup

Check running containers:

```bash
docker ps
```

Access the API:

```bash
curl http://localhost:8000/
```

---

## Step 7: Connect to PostgreSQL Database

Enter the PostgreSQL container:

```bash
docker exec -it postgres-container psql -U admin -d db
```

**Useful PostgreSQL commands:**

```sql
-- List all databases
\l

-- Connect to the 'db' database
\c db

-- List all tables
\dt

-- View trending AI posts
SELECT * FROM public.trending_ai_posts;

-- Exit PostgreSQL
\q
```

---

## Step 8: Test the API

Fetch trending AI tools from Reddit and store in database:

```bash
curl http://localhost:8000/trending-ai-tools
```

---

## Stopping & Cleaning Up

Stop containers:

```bash
docker stop fast-api-container postgres-container
```

Remove containers:

```bash
docker rm fast-api-container postgres-container
```

Remove network:

```bash
docker network rm fast-api-network
```

---

## Troubleshooting

### Containers won't communicate

- Ensure both containers are on the same network
- Check network: `docker network ls`

### Port already in use

- Change the port mapping: `-p 9000:8000` for FastAPI or `-p 5433:5432` for PostgreSQL

### PostgreSQL connection refused

- Wait a few seconds for PostgreSQL to start
- Check logs: `docker logs postgres-container`
