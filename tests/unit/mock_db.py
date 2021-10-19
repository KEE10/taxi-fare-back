from unittest import TestCase
from mock import patch

from services import database


MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "testdb"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"


class MockDB(TestCase):
    @classmethod
    def setUpClass(cls):
        db_test_config = {
            "host": MYSQL_HOST,
            "user": MYSQL_USER,
            "password": MYSQL_PASSWORD,
            "port": MYSQL_PASSWORD
        }

        # drop database if it already exists
        database.drop_db("TaxiFare", db_test_config)

        # create database
        database.create_database("TaxiFare", db_test_config)

        # create table in database
        database.create_rides_table(db_test_config)

        # insert dummy data in table
        insert_data_query = """INSERT INTO `Rides` (`Id`, `Distance`, `StartTime`, `Duration`) VALUES
                            (1, 9, '2020-06-19T19:01:17,031Z', 9000),
                            (2, 7, '2020-06-19T17:01:17,031Z', 7000),
                            (3, 2, '2020-06-19T13:01:17,031Z', 3000)"""
        database.insert_data_to_table(insert_data_query, db_test_config)

        cls.mock_db_config = patch.dict(database.db_config, db_test_config)

    @classmethod
    def tearDownClass(cls):
        db_test_config = {
            "host": MYSQL_HOST,
            "user": MYSQL_USER,
            "password": MYSQL_PASSWORD,
            "port": MYSQL_PASSWORD
        }

        # drop database
        database.drop_db("TaxiFare", db_test_config)
