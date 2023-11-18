# panxml2json

Convert Palo Alto 8.1 XML API calls to standard JSON



## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Configuration

Use `settings.yaml` to populate a drop-down menu of Management servers

#### Example

```
devices:
  - 
    hostname: firewall1.mydomain.com
    api_key: abcd1234
  - 
    hostname: firewall2.mydomain.com
    api_key: efgh5678

google_maps_api_key: xxxxxx
```
### Configuring From Files

## Usage

Run via Flask:

```
python wsgi.py
```

or 

```
flask run
```

For increased performance, run via hypercorn:

```
gunicorn --access-logfile '-' wsgi:app
```

### Running in Docker

```

docker build -t panxml2json .

docker run -p 8000:8000 --name panxml2json panxml2json 

```

## Reference


## Changelog

- Version 0.1 : initial upload
