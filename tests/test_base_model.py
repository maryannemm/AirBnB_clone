#!/usr/bin/python3
"""
Test module for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """
    def test_base_model_attributes(self):
        """
        Test attributes of the BaseModel class.
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_base_model_str(self):
        """
        Test the __str__ method of the BaseModel class.
        """
        my_model = BaseModel()
        str_representation = "[BaseModel] ({}) {}".format(my_model.id,
                                                           my_model.__dict__)
        self.assertEqual(str(my_model), str_representation)

    def test_base_model_save(self):
        """
        Test the save method of the BaseModel class.
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue('__class__' in my_model_dict)
        self.assertTrue('created_at' in my_model_dict)
        self.assertTrue('updated_at' in my_model_dict)
        self.assertTrue('id' in my_model_dict)

if __name__ == "__main__":
    unittest.main()

