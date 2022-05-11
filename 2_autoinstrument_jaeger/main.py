import flask
import requests
import json
from flask_cors import CORS

## Instrument code for opentelemetry and jaeger ###
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({SERVICE_NAME: "products-services"})
    )
)

jaeger_exporter = JaegerExporter(
    agent_host_name="192.168.10.223",
    agent_port=6831,
)


app = flask.Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

tracer = trace.get_tracer(__name__)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)
## Instrument code for opentelemetry and jaeger ###

cors = CORS(app)

products = list()
products.append({"id":1, "name" : "Leche", "cost" : 500})
products.append({"id":2, "name" : "Cafe", "cost" : 600})
products.append({"id":3, "name" : "Azucar", "cost" : 300})
products.append({"id":4, "name" : "Arroz", "cost" : 400})

# expose a GET service over /, return all objects in the list
@app.route('/', methods=['GET'])
def get_products():
    jsonString = json.dumps(products)
    return jsonString


# expose a GET service over /product/{id}, return a product from id
@app.route('/product/<id>', methods=['GET'])
def get_product(id=None):
    jsonString = json.dumps(products[int(id)])
    return jsonString


# expose a POST serice over /product, add objects to the list
@app.route('/product/<id>/<name>/<cost>', methods=['POST'])
def add_product(id=None, name=None, cost=None):
    products.append({"id":id, "name" : name, "cost" : cost})
    return "200"


# expose service DELETE over /product/{id}, delete a id element from list
@app.route('/producto/<id>', methods=['DELETE'])
def delete_producto(id=None):
    for prod in product:
        if str(prod["id"]) == id:
            product.remove(prod)
            break
    return "200"
