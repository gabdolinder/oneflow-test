import mysql.connector
import subprocess

"""
This file creates the connection, the databases and creates the needed tables
It also contains functions that selects and inserts data into the tables
"""

CREATE_USER_ANALYTICS_TABLE = f"""CREATE TABLE IF NOT EXISTS user_analytics (
  id INT PRIMARY KEY,
  email VARCHAR(255),
  firstname VARCHAR(255),
  lastname VARCHAR(255),
  language VARCHAR(50),
  timezone VARCHAR(50),
  is_stakeholder BOOLEAN,
  last_visit_time DATETIME,
  role VARCHAR(50),
  account_id INT,
  updated DATETIME,
  created DATETIME
)"""

CREATE_ACCOUNT_ANALYTICS_TABLE = f"""CREATE TABLE IF NOT EXISTS account_analytics (
  id INT PRIMARY KEY,
  is_demo BOOLEAN,
  plan VARCHAR(50),
  license_count INT,
  user_count INT,
  purchase_time DATETIME,
  customer_io_opted_in BOOLEAN,
  last_visit_time DATETIME,
  updated DATETIME,
  created DATETIME
)"""


def create_connection():
    """Create a database connection to a MySQL server"""
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="your user",               #change user
            password="your password"        #change password
        )
        print("Connection established")
        return mydb
    except mysql.connector.Error as e:
        print(e)
        return None


def create_databases(connection):
    """Create production and analytics databases if they don't exist"""
    try:
        mycursor = connection.cursor()
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS production")
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS analytics")
        print(f"Databases created successfully.")
    except mysql.connector.Error as e:
        print(e)


def create_prod_tables(sql_file):
    """Creates and populates the production tables"""
    try:
        subprocess.run(
            ["mysql", "-u", "your user", "-p", "your password", "-D", "production", "-e", f"source {sql_file}"], #change user and password
            check=True,
        )
        print("SQL file executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing SQL file: {e}")


def create_analytics_tables(connection):
    """Create analytics tables"""
    try:
        mycursor = connection.cursor()
        mycursor.execute("USE analytics")
        mycursor.execute(CREATE_USER_ANALYTICS_TABLE)
        mycursor.execute(CREATE_ACCOUNT_ANALYTICS_TABLE)
        print("Analytics tables created successfully.")
    except mysql.connector.Error as e:
        print(e)


def fetch_and_insert_data(connection, source_table, destination_table):
    """Fetches and inserts data from the production table into the analytics table"""
    select_query = f"SELECT * FROM production.{source_table}"
    try:
        mycursor = connection.cursor()
        mycursor.execute("USE analytics")
        insert_query = (
            f"INSERT INTO {destination_table} SELECT * FROM ({select_query}) AS tmp"
        )
        mycursor.execute(insert_query)
        connection.commit()
        print(f"Data inserted successfully into {destination_table}.")
    except mysql.connector.Error as e:
        print(e)
