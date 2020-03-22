# Part 4: Deploying a container service

Run all the commands as administrator.

## Docker build
```bash
docker build -t flask-prediction:latest .
```

## Docker run
```bash
docker run -d -p 5000:5000 flask-prediction
```

## Docker compose
```bash
docker-compose up
```

## cURL GET
```bash
curl 0.0.0.0:5000/predict?input=this+sucks
```

## cURL POST
```bash
curl -d '{"input":"this is great"}' localhost:5000/predict
```
