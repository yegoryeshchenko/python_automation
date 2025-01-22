import os
import time

import psycopg2
import pytest


@pytest.fixture(scope="module")
def db_connection():
    time.sleep(1)
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "pg_db"),
        port=os.getenv("DB_PORT", "5433"),
        database=os.getenv("DB_NAME", "test_db"),
        user=os.getenv("DB_USER", "test_user1"),
        password=os.getenv("DB_PASSWORD", "test_password"),
    )
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def setup_test_table(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        );
    """)
    db_connection.commit()
    yield
    cursor.execute("DROP TABLE IF EXISTS test_table;")
    db_connection.commit()
    cursor.close()


def test_insert_data(db_connection, setup_test_table):
    cursor = db_connection.cursor()
    cursor.execute("""
        INSERT INTO test_table (name, age) VALUES
        ('Alice', 25),
        ('Bob', 30);
    """)
    db_connection.commit()
    cursor.close()


def test_select_data(db_connection, setup_test_table):
    cursor = db_connection.cursor()

    cursor.execute("""
        INSERT INTO test_table (name, age) VALUES
        ('test_user_1', 23),
        ('test_user_2', 76);
    """)
    db_connection.commit()

    cursor.execute("SELECT * FROM test_table;")
    results = cursor.fetchall()
    assert len(results) == 2
    assert results[0][1] == 'test_user_1'
    assert results[1][1] == 'test_user_2'
    cursor.close()
