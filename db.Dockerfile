# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the application files into the container
COPY . /app

# 4. Install necessary Python dependencies
#    - Use requirements.txt for cleaner dependency management
RUN pip install --no-cache-dir -r requirements.txt

# 5. Set environment variables to match your database config
#    - These values can be overridden by docker-compose.yaml or CLI
ENV DB_HOST=pg_db \
    DB_PORT=5433 \
    DB_NAME=test_db \
    DB_USER=test_user1 \
    DB_PASSWORD=test_password

# 6. Define the default command to run tests
CMD ["pytest"]