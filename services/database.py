import os

import mysql.connector
from mysql.connector import errorcode


DB_CONFIG = {
    "host": os.environ["host"],
    "database": "TaxiFare",
    "user": os.environ["user"],  # TODO: store secrets in a more secure way
    "password": os.environ["password"]
}


def create_database(database, db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
    else:
        connection.database = database
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


def create_rides_table(db_config):
    try:
        connection = mysql.connector.connect(**db_config)
        create_table_query = """CREATE TABLE Rides ( 
                                     Id INT NOT NULL,
                                     Distance FLOAT NOT NULL,
                                     StartTime VARCHAR NOT NULL,
                                     Duration FLOAT NOT NULL,
                                     PRIMARY KEY (Id)) """

        cursor = connection.cursor()
        cursor.execute(create_table_query)
        print("Laptop Table created successfully ")

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Rides table already exists.")
        else:
            print("Failed to create table in MySQL: {}".format(error))

    else:
        connection.close()

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def drop_db(database, db_config):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute("DROP DATABASE {}".format(database))
        cursor.close()
        print(f"{database} DB dropped")
    except mysql.connector.Error as err:
        print("{}{}".format(database, err))
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


def insert_data_to_table(query, db_config):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    insert_data_query = query
    try:
        cursor.execute(insert_data_query)
        connection.commit()
    except mysql.connector.Error as error:
        print(f"Data insertion to rides table failed. {error}")
    cursor.close()
    connection.close()
    print("MySQL connection is closed")


def fetch_all_rides(db_config):
    try:
        connection = mysql.connector.connect(**db_config)

        select_query = "select * from Rides"
        cursor = connection.cursor()
        cursor.execute(select_query)
        # get all records
        records = cursor.fetchall()
        rides = []
        for row in records:
            rides.append({
                "id": row[0],
                "distance": row[1],
                "startTime": row[2],
                "duration": row[3]
            })

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User authorization error")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        else:
            print(error)
        return None

    else:
        connection.close()

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
        return rides
