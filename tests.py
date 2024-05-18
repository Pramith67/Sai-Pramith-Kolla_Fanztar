import unittest
import json
from main import app


class TestOrderSystem(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_order_valid_components(self):
        payload = {"components": ["I", "A", "D", "F", "K"]}
        response = self.app.post('/order', json=payload)
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertIn('order_id', data)
        self.assertIn('total', data)
        self.assertIn('parts', data)

    def test_create_order_invalid_component(self):
        payload = {"components": ["Z"]}
        response = self.app.post('/order', json=payload)
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid component code')

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Mobile Phone order system')


if __name__ == "__main__":
    unittest.main()
