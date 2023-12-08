docker build . -t tda-flask
docker run -p 8080:80 -v ${PWD}:/app tda-flask