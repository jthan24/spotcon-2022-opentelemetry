
# How to run this app

## Start jaeger service over docker for metrics importer
```bash
docker run -p 16686:16686 -p 6831:6831/udp -p 5778:5778 --rm --name jaeger-server jaegertracing/all-in-one 
docker run -p 16686:16686 -p 6831:6831/udp -p 5778:5778 --rm -d --name jaeger-server jaegertracing/all-in-one 
```

## Start browins with at this link
http://localhost:16686/

http://192.168.10.223:16686/search
