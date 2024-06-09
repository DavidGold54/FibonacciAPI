FROM python:slim

WORKDIR /FibonacciAPI

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--reload"]