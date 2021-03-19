FROM python:3.8

COPY . /furia-site

WORKDIR /furia-site

RUN pip install -r requirements.txt

WORKDIR /furia-site/src

CMD ["gunicorn", "app:app", "-b", ":8000", "-t", "1200"]