
from flask import Flask
from flask import request
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)


tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("products"):
    with tracer.start_as_current_span("service"):
            print("Hello world from OpenTelemetry Python!")

import json

app = Flask(__name__)

products = list()
products.append({"id":1, "name" : "Leche", "value" : 500})
products.append({"id":2, "name" : "Cafe", "value" : 600})
products.append({"id":3, "name" : "Azucar", "value" : 300})
products.append({"id":4, "name" : "Arroz", "value" : 400})


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
@app.route('/product/<id>/<name>/<value>', methods=['POST'])
def add_product(id=None, name=None, value=None):
    products.append({"id":id, "name" : name, "value" : value})
    return "200"


# expose service DELETE over /product/{id}, delete a id element from list
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id=None):
    products.remove(products[int(id)])
    return "200"
