# استخدم صورة Python
FROM python:3.11-slim

# حطي الكود جوا الكونتينر
WORKDIR /app
COPY calculator.py .

# الأمر اللي يشتغل
CMD ["python", "calculator.py"]
