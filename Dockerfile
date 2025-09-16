FROM python:3.13-slim

WORKDIR /app
COPY calculator.py .
COPY test_calculator.py .

CMD ["python", "calculator.py"]
