ROM python:3.10-slim

WORKDIR /app

COPY ./main.py /app

COPY ./requirements.txt /app

EXPOSE 80000

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80000"]