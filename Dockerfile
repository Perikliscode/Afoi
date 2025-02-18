FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt .
COPY FrontEnd/ /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "FrE.py"]