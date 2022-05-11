
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

docker build . --tag python-autoinstrument
docker run -p 5000:5000 --name python-autoinstrument --rm python-autoinstrument:latest

## Check current app
http://127.0.0.1:5000


# For run this app in debug mode

export FLASK_DEBUG=1
export FLASK_ENV=development
