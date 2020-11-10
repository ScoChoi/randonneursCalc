FROM python:3
MAINTAINER Scott Choi "ascottychoi@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /flask_brevets.py
WORKDIR /flask_brevets.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask_brevets.py"]
