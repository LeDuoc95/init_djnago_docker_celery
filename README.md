# (TODO)
## Api document
[Postman document](https://documenter.getpostman.com/view/4119643/S1TN8heC?version=latest)

## Evironment
- python: 3.7
## Setup
[Intall virtualevn](https://pypi.org/project/virtualenv/)
```bash
$ git clone "replace by git"

$ virtualenv venv

$ source venv/bin/activate

$ cd "workdir"

$ touch config/settings/default.py

$ pip install -r requirements.txt

$ python manage migate

$ python manage runserver
```
## Testing
```bash
$ pytest
```

## lint and check code
Docs: http://pycodestyle.pycqa.org/en/latest/intro.html#error-codes
```bash
$ pycodestyle --exclude migrations --show-source --show-pep8 puppies
```

## (TODO) check coding convention
```bash
$ python manage.py lint_code
$ python manage.py initial_data region
$ python manage.py initial_data area
$ python manage.py initial_data ward
$ python manage.py initial_data region

```


## Run with docker, docker-compose (assume that docker and docker-compose were installed)
```bash
$ docker-compose up -d
```
### Start develop env
```bash
docker-compose -f docker-compose.yml up -d --build database 
docker-compose -f docker-compose.yml up -d --build api_dev migration_dev 
```
### Start testing env
```bash
docker-compose -f docker-compose.yml up -d --build database 
docker-compose -f docker-compose.yml up -d --build api_test migration_test 
```
### Start staging env
```bash
docker-compose -f docker-compose.yml up -d --build database 
docker-compose -f docker-compose.yml up -d --build api_stg migration_stg 
```

### Change for push test