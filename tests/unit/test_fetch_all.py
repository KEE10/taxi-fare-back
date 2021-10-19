from mock_db import MockDB
from services import database


class TestUtils(MockDB):
    def test_fetch(self):
            self.assertEqual(database.fetch_all_rides(self.mock_db_config), [
                {
                    "id": 1,
                    "distance": 9,
                    "startTime": "2020-06-19T19:01:17,031Z",
                    "duration": 9000
                },
                {
                    "id": 2,
                    "distance": 7,
                    "startTime": "2020-06-19T17:01:17,031Z",
                    "duration": 7000
                },
                {
                    "id": 3,
                    "distance": 3,
                    "startTime": "2020-06-19T13:01:17,031Z",
                    "duration": 3000
                }
            ])
