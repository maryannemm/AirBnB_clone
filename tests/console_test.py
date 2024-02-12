import unittest
from models import storage
from models.user import User
from console import HBNBCommand
from io import StringIO
import sys


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures, such as creating instances of classes."""
        self.cmd = HBNBCommand()
        self.test_user = User()

    def tearDown(self):
        """Tear down test fixtures, if necessary."""
        storage.delete(self.test_user)

    def test_create(self):
        """Test the create command."""
        # Test creating a new instance
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('create User')
            new_user_id = fake_out.getvalue().strip()
            self.assertIn(new_user_id, storage.all())
            self.assertTrue(isinstance(storage.all()[new_user_id], User))

    # Add more test methods for other commands such as show, destroy, update, etc.

    def test_all(self):
        """Test the all command."""
        # Test retrieving all instances
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('all')
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)
            # Check if output contains the string representation of instances

    def test_count(self):
        """Test the count command."""
        # Test counting instances of a class
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('count User')
            output = fake_out.getvalue().strip()
            self.assertTrue(output.isdigit())

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()

