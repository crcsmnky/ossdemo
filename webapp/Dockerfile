FROM python:2

COPY . /app/

RUN pip install -r /app/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/app/webapp.py"]