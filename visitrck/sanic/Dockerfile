FROM python:3.6
RUN mkdir -p /srv/app
WORKDIR /srv/app
COPY requirements.txt /srv/app/
RUN pip install -r requirements.txt
COPY . /srv/app
CMD ["gunicorn", "serv:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker"]


