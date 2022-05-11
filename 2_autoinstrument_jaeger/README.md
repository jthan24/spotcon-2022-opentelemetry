
# Run this app locally

## How to run this app

python3 -m venv venv
. venv/bin/activate
pip install flask
pip install requests
pip install opentelemetry-distro
pip install opentelemetry-instrumentation-flask

export FLASK_APP=main
flask run

## Check current app
http://127.0.0.1:5000

pip freeze > requirements.txt

# Run this app in Docker

## How to run this app

docker build . --tag jaeger-python-autoinstrument

## Start application in multiples ports
docker run -p 5000:5000 --name jaeger-python-autoinstrument0 --rm -d jaeger-python-autoinstrument:latest
docker run -p 5001:5000 --name jaeger-python-autoinstrument1 --rm -d jaeger-python-autoinstrument:latest
docker run -p 5002:5000 --name jaeger-python-autoinstrument2 --rm -d jaeger-python-autoinstrument:latest


## Stop application 
docker stop jaeger-python-autoinstrument0
docker stop jaeger-python-autoinstrument1
docker stop jaeger-python-autoinstrument2

## Check current app
http://127.0.0.1:5000


# For run this app in debug mode

export FLASK_DEBUG=1
export FLASK_ENV=development


# Send metrics to current app
curl -X GET 'http://192.168.10.223:5000/' -H 'User-Agent: Mozilla/5.0' 
curl -X GET 'http://192.168.10.223:5001/' -H 'User-Agent: InternetExplorer/9.0' 
curl -X GET 'http://192.168.10.223:5002/' -H 'User-Agent: Brave/20.0' 


curl -X GET 'http://192.168.10.223:5000/product/1' -H 'User-Agent: Mozilla/5.0' 
curl -X GET 'http://192.168.10.223:5000/product/1' -H 'User-Agent: InternetExplorer/9.0' 
curl -X GET 'http://192.168.10.223:5000/product/1' -H 'User-Agent: Brave/20.0' 



curl -X GET 'http://192.168.10.223:5000/product/10' -H 'User-Agent: Mozilla/5.0' 
curl -X GET 'http://192.168.10.223:5000/product/11' -H 'User-Agent: InternetExplorer/9.0' 
curl -X GET 'http://192.168.10.223:5000/product/12' -H 'User-Agent: Brave/20.0' 



for i in $(seq 1 10) ; do curl -X GET "http://192.168.10.223:5000/product/$i" -H 'User-Agent: Mozilla/5.0' ; sleep 0.2 ; done && 
for i in $(seq 1 10) ; do curl -X GET "http://192.168.10.223:5001/product/$i" -H 'User-Agent: Mozilla/5.0' ; sleep 0.2 ; done &&
for i in $(seq 1 10) ; do curl -X GET "http://192.168.10.223:5002/product/$i" -H 'User-Agent: Mozilla/5.0' ; sleep 0.2 ; done 




for i in $(seq 1 10) ; do curl -X GET "http://192.168.10.223:5000/" -H 'User-Agent: Mozilla/5.0' ; sleep 0.2 ; done && 
for i in $(seq 1 10) ; do curl -X GET "http://192.168.10.223:5001/" -H 'User-Agent: Mozilla/5.0' ; sleep 0.2 ; done &&
for i in $(seq 1 10) ; do curl -X GET "http://192.168.10.223:5002/" -H 'User-Agent: Mozilla/5.0' ; sleep 0.2 ; done 
