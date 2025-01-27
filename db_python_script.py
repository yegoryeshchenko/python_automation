import os
import psycopg2
import time


time.sleep(1)  # бд може ініціалізуватись не миттево
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
)
print("Connected to the database!")
