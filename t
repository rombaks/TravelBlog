[1mdiff --git a/docker-compose.ci.yml b/docker-compose.ci.yml[m
[1mindex cf91456..b7d94f1 100644[m
[1m--- a/docker-compose.ci.yml[m
[1m+++ b/docker-compose.ci.yml[m
[36m@@ -1,17 +1,18 @@[m
 version: "3.7"[m
 [m
 x-app-config: &app-config[m
[31m-  DJANGO_ENV: dev[m
[31m-  DJANGO_SECRET_KEY: secret_key[m
[32m+[m[32m  DJANGO_ENV: ${DJANGO_ENV}[m
[32m+[m[32m  DJANGO_SECRET_KEY: ${DJANGO_SECRET_KEY}[m
   COVERALLS_REPO_TOKEN: ${COVERALLS_REPO_TOKEN}[m
 [m
 x-db-config: &db-config[m
[31m-  DATABASE_NAME: postgres[m
[31m-  DATABASE_USER: postgres[m
[31m-  DATABASE_PASSWORD: pgpassword[m
[31m-  DATABASE_HOST: db[m
[31m-  DATABASE_PORT: 5432[m
[31m-  POSTGRES_PASSWORD: pgpassword[m
[32m+[m[32m  DATABASE_NAME: ${DATABASE_NAME}[m
[32m+[m[32m  DATABASE_USER: ${DATABASE_USER}[m
[32m+[m[32m  DATABASE_PASSWORD: ${DATABASE_PASSWORD}[m
[32m+[m[32m  DATABASE_HOST: ${DATABASE_HOST}[m
[32m+[m[32m  DATABASE_PORT: ${DATABASE_PORT}[m
[32m+[m[32m  CELERY_BROKER_URL: ${CELERY_BROKER_URL}[m
[32m+[m[32m  CELERY_RESULT_BACKEND: ${CELERY_RESULT_BACKEND}[m
 [m
 services:[m
   api:[m
[36m@@ -22,6 +23,7 @@[m [mservices:[m
       <<: *app-config[m
       <<: *db-config[m
     depends_on:[m
[32m+[m[32m      - redis[m
       - db[m
     ports:[m
       - "8000:8000"[m
[36m@@ -36,5 +38,34 @@[m [mservices:[m
     ports:[m
       - "5432:5432"[m
 [m
[32m+[m[32m  redis:[m
[32m+[m[32m    image: redis:7-alpine[m
[32m+[m
[32m+[m[32m  celery:[m
[32m+[m[32m    build: .[m
[32m+[m[32m    command: celery worker --app=travel_blog --loglevel=info --logfile=logs/celery.log[m
[32m+[m[32m    volumes:[m
[32m+[m[32m      - .:/app[m
[32m+[m[32m    environment:[m
[32m+[m[32m      <<: *app-config[m
[32m+[m[32m      <<: *db-config[m
[32m+[m[32m    depends_on:[m
[32m+[m[32m      - api[m
[32m+[m[32m      - redis[m
[32m+[m
[32m+[m[32m  flower:[m
[32m+[m[32m    build: .[m
[32m+[m[32m    command: celery -A travel_blog --broker=redis://redis:6379/0 flower --port=5555[m
[32m+[m[32m    ports:[m
[32m+[m[32m      - 5555:5555[m
[32m+[m[32m    environment:[m
[32m+[m[32m      <<: *app-config[m
[32m+[m[32m      <<: *db-config[m
[32m+[m[32m    depends_on:[m
[32m+[m[32m      - api[m
[32m+[m[32m      - redis[m
[32m+[m[32m      - celery[m
[32m+[m
[32m+[m
 volumes:[m
   sqlvolume:[m
\ No newline at end of file[m
