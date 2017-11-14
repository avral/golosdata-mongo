FROM python:3.6.2
MAINTAINER avral <tg:@avral>

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/src

CMD ["python", "__main__.py"]
