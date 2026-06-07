1 - please make sure, you create your Dockerfile
2 - cretae an image for fast-api-app using => docker build -t fast-api-image .
3 - see your images list => docker images
4 - get latest postgres image from docker Hub => docker pull postgres

5 - create a docker network => docker network create fast-api-network
6 - create 2 containers, one for postgress and the other one for fast-api-app, make sur connect both conatiners on the same network just created.

=> For postgres: docker run -d --name postgres-container --network fastapi-network -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=root -e POSTGRES_DB=db -p 5432:5432 postgres

=> For fast api= => docker run -d --name fast-api-container --network fastapi-network -p 8000:8000 fast-api-image

7 - make sure to explore your postgres db, by connecting to postgres container using
=> docker -exec -it postgres-container

then connect to postgres db, and explore trending_ai_posts table

=> psql -U admin -d db
=> \l (list databases)
=> \c db (connect to db database)
=> \dt (list tables)
=> select from public.trending_ai_posts (explore trending_ai_posts table)
