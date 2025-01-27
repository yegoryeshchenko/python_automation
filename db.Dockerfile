
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install allure-pytest

# Set environment variables to match your database config
ENV DB_HOST=pg_db \
    DB_PORT=5433 \
    DB_NAME=test_db \
    DB_USER=test_user1 \
    DB_PASSWORD=test_password

CMD ["pytest", "allure generate allure-results -o allure-report --alluredir=/app/allure-results", "lesson_30_dockerize/test_db_python_script.py"]
