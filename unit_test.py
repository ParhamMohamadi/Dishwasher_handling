import unittest
from dish_handeling import DishHandling

class TestDishHandling(unittest.TestCase):

    def setUp(self):
        self.dish_1 = {
            'name': 'Tea cup',
            'type': 'Cup',
            'have_time': True,
            'washer_running': False,
            'washer_full': True,
            'inside_dirty_dishes': False
        }
        self.dish_2 = {
            'name': 'fork',
            'type': 'Cutlery',
            'have_time': True,
            'washer_running': True,
            'washer_full': True,
            'inside_dirty_dishes': False
        }
        self.dish_3 = {
            'name': 'launch plate',
            'type': 'Plate',
            'have_time': True,
            'washer_running': False,
            'washer_full': False,
            'inside_dirty_dishes': False
        }

    def test_get_dish_handling_status(self):
        # Test for dish_1
        dish_instance = DishHandling(name=self.dish_1['name'], dish_type=self.dish_1['type'])
        dish_instance.have_time = self.dish_1['have_time']
        dish_instance.washer_running = self.dish_1['washer_running']
        dish_instance.washer_full = self.dish_1['washer_full']
        dish_instance.inside_dirty_dishes = self.dish_1['inside_dirty_dishes']

        # Vérifie que la méthode s'exécute sans erreur
        try:
            dish_instance.get_dish_handling_status()
        except Exception as e:
            self.fail(f"get_dish_handling_status() raised {type(e).__name__} unexpectedly!")

        # Test for dish_2
        dish_instance = DishHandling(name=self.dish_2['name'], dish_type=self.dish_2['type'])
        dish_instance.have_time = self.dish_2['have_time']
        dish_instance.washer_running = self.dish_2['washer_running']
        dish_instance.washer_full = self.dish_2['washer_full']
        dish_instance.inside_dirty_dishes = self.dish_2['inside_dirty_dishes']

        # Vérifie que la méthode s'exécute sans erreur
        try:
            dish_instance.get_dish_handling_status()
        except Exception as e:
            self.fail(f"get_dish_handling_status() raised {type(e).__name__} unexpectedly!")

        # Test for dish_3
        dish_instance = DishHandling(name=self.dish_3['name'], dish_type=self.dish_3['type'])
        dish_instance.have_time = self.dish_3['have_time']
        dish_instance.washer_running = self.dish_3['washer_running']
        dish_instance.washer_full = self.dish_3['washer_full']
        dish_instance.inside_dirty_dishes = self.dish_3['inside_dirty_dishes']

        # Vérifie que la méthode s'exécute sans erreur
        try:
            dish_instance.get_dish_handling_status()
        except Exception as e:
            self.fail(f"get_dish_handling_status() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
