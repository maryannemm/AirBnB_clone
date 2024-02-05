import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("all User")
            self.assertIn("[User] ", f.getvalue())

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("count User")
            self.assertIn("2", f.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            user_id = output[output.find("(") + 1:output.find(")")]
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn(f"[User] ({user_id})", f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            user_id = output[output.find("(") + 1:output.find(")")]
            HBNBCommand().onecmd(f"destroy User {user_id}")
            HBNBCommand().onecmd("all User")
            self.assertNotIn("[User] ({user_id})", f.getvalue())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            user_id = output[output.find("(") + 1:output.find(")")]
            HBNBCommand().onecmd(f"update User {user_id} first_name 'John'")
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn("'first_name': 'John'", f.getvalue())

    def test_update_from_dict(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            user_id = output[output.find("(") + 1:output.find(")")]
            HBNBCommand().onecmd(f"update User {user_id} {{'first_name': 'John', 'age': 30}}")
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn("'first_name': 'John'", f.getvalue())
            self.assertIn("'age': 30", f.getvalue())

    def test_invalid_commands(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("some_invalid_command")
            self.assertIn("**", f.getvalue())


if __name__ == "__main__":
    unittest.main()

