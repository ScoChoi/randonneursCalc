docker rm $(docker ps -a -q)
docker build -t flask-brevets:latest .
docker run -d -p 5000:5000 flask-brevets
