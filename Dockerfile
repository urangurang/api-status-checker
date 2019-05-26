FROM python:3.6

RUN mkdir -p /src/app/
WORKDIR /src/app/

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]