### Run the Dev server 
```bash
python manage.py runserver
```

### Install Redis
```bash
https://redis.io/docs/getting-started/
```

### Run Redis Server for Temporarily
```bash
redis-cli
```

### Open new terminal tab and test the redis server is working
```bash
redis-cli ping
output: PONG
```

### Create new app or module 
```bash
python manage.py startapp exampleapp 
```

### Migrations and Migrate 
a) Migrations
For All apps 
```bash
python manage.py makemigrations
```
For specific app
```bash
python manage.py makemigrations app_name
```

b) Migrate 
For All apps 
```bash
python manage.py migrate
```
For specific app
```bash
python manage.py migrate app_name
```