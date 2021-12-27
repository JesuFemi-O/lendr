FROM python:3.9
ENV PYTHONUNBUFFERED=1

COPY ./custom_server /app/custom_server
COPY ./.env /app/.env
COPY ./assets /app/assets
COPY ./requirements.txt /app
COPY gunicorn-config.py /app

WORKDIR /app

RUN pip install -r requirements.txt


# CMD ["uvicorn", "custom_server.main:app", "--host=0.0.0.0", "--reload"]
CMD exec gunicorn custom_server.main:app -c gunicorn-config.py