
# Manage Url API  

This API provides functionality for shortening your url.

## Requirements:

- [Install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)
- [Install Docker Compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)

## Steps:

### Build project:
```commandline
docker-compose build
```  
### Run project:
```commandline
docker-compose up -d
```

### Migrate database:
```commandline
docker-compose exec app ./manage.py migrate
```

### Run tests:
```commandline
docker-compose exec app ./manage.py test
```

### See in web
Check Django project in [browser](http://localhost:8000/)

## Examples  

----
[shorten_endpoint](http://localhost:8000/url/shorten/)
```json
{
  "url": "https://github.com/ellisonleao/pyshorteners/"
}
```

## Helpers  

----

### Stop project
```commandline
docker-compose stop
```

### Remove project
```commandline
docker-compose down
```