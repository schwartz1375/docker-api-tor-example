## Project Structure
The project structure will be as follows:
```
|-- app/
|   |-- __init__.py
|   |-- routes.py
|   |-- scraper.py
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- run.py
```

## API Documentation
Refer to the comments in the app/routes.py for endpoint details. Basically, we have two endpoints:

1. GET /api/ips: Fetches IPs from external sources excluding the ones in the database.
2. POST /api/exclude-ip: Receives an IP and adds it to the exclusion database.

## How to Run
Development
1. Create a virtual environment and install the dependencies:
```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
2. Run the application:
```
python run.py
```

## Production
Build and run the Docker container using Docker Compose:
```
docker-compose build --no-cache
docker-compose up
```

## To Test the Endpoints
* Get IPs: You can make a GET request to get the IPs. Since it's a GET request, you can simply open http://127.0.0.1:6000/api/ips in your web browser, or use a tool like curl:

```
curl http://127.0.0.1:6000/api/ips
```

Note that ```https://www.dan.me.uk/torlist/?exit``` has rate limiting and this can be addressed with multiple methods (i.e. proxies, delays, etc). 

* Exclude IP: To exclude an IP, you need to make a POST request. You can use curl for this as well, replacing "x.x.x.x" with the IP you want to exclude:

```
curl -X POST -H "Content-Type: application/json" -d '{"ip":"x.x.x.x"}' http://127.0.0.1:6000/api/exclude-ip
```
Replace "x.x.x.x" with the actual IP address that you want to exclude.

```
% curl http://127.0.0.1:6000/api/ips                                                     
[
  "104.219.236.93",
  "80.241.60.207",
  "185.220.102.242",
  "2001:067c:06ec:0203:0192:0042:0116:0188",
  "2a0b:f4c2:0000:0000:0000:0000:0000:0016",
  "45.141.215.81",
  "23.154.177.25",
  ....[REDUCED FOR BREVIARY]....
  "2a0b:f4c0:016c:0003:0000:0000:0000:0001",
  "125.212.241.131",
  "199.249.230.189",
  "2001:067c:06ec:0203:0192:0042:0116:0183",
  "185.220.102.243",
  "23.129.64.226",
  "45.95.169.226",
  "45.95.169.228",
  "185.195.71.11",
  "185.220.101.183",
  "23.154.177.2",
  "194.233.88.182",
  "95.181.161.159"
]
% curl -X POST -H "Content-Type: application/json" -d '{"ip":"95.181.161.159"}' http://127.0.0.1:6000/api/exclude-ip
{
  "message": "IP excluded successfully"
}
% curl http://127.0.0.1:6000/api/ips  
  "104.219.236.93",
  "80.241.60.207",
  "185.220.102.242",
  "2001:067c:06ec:0203:0192:0042:0116:0188",
  "2a0b:f4c2:0000:0000:0000:0000:0000:0016",
  "45.141.215.81",
  "23.154.177.25",
  ....[REDUCED FOR BREVIARY]....
  "2a0b:f4c0:016c:0003:0000:0000:0000:0001",
  "125.212.241.131",
  "199.249.230.189",
  "2001:067c:06ec:0203:0192:0042:0116:0183",
  "185.220.102.243",
  "23.129.64.226",
  "45.95.169.226",
  "45.95.169.228",
  "185.195.71.11",
  "185.220.101.183",
  "23.154.177.2",
  "194.233.88.182",
  "95.181.161.159"
]
```
