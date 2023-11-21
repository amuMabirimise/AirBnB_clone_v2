#!/usr/bin/python3
"""Test module for Amenity class."""
import unittest
import MySQLdb
from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel

DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database_name'

class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up test environment."""
        super().setUp()
        self.cls = Amenity
        self.obj = self.cls()

    def tearDown(self):
        """Tear down test environment."""
        super().tearDown()

    @unittest.skipIf(storage_type != 'db', 'Test not applicable for this storage type')
    def test_name_type(self):
        """Test that the 'name' attribute is of type str."""
        new = self.cls()
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(storage_type != 'db', 'Test not applicable for this storage type')
    def test_create_amenity_in_db(self):
        """Test creating Amenity instance adds a record in the database."""
        initial_count = self.get_amenity_count()

        execute_console_command('create Amenity name="California"')

        final_count = self.get_amenity_count()

        self.assertEqual(final_count - initial_count, 1)

    def get_amenity_count(self):
        """Get the number of current records in the 'amenities' table."""
        try:
            connection = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM amenities;")
            count = cursor.fetchone()[0]
            return count
        finally:
            if connection:
                connection.close()

def execute_console_command(command):
    """Execute the given console command."""
    with unittest.mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        unittest.mock.patch('sys.stdin', StringIO(command)).__enter__()
        try:
            unittest.main(argv=[''])
        except SystemExit:
            pass
        return mock_stdout.getvalue().strip()

if __name__ == '__main__':
    unittest.main()

