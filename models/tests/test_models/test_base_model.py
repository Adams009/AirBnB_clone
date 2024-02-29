#!/usr/bin/python3
"""
the test for BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()

        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_save(self):
        my_model = BaseModel()
        init_update = my_model.updated_at
        current = my_model.save()
        self.assertNotEqual(init_update, current)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], my__model.updated_at.isoformat())
        self.assertEqual(my_model_dict['id'], my_model.id)

    def test_str(self):
        my_model = BaseModel()
        init_str = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), init_str)

if __name__ == '__main__':
    unittest.main()
