from dish_handeling import DishHandling

# valid dish types are: ["Cup", "Glass", "Cutlery", "Plate", "Bowl"]

if __name__ == '__main__':
    dish_1 = {
        'name': 'Tea cup',
        'type': 'Cup',
        'have_time': True,
        'washer_running': False,
        'washer_full': True,
        'inside_dirty_dishes': False
    }
    dish_2 = {
        'name': 'fork',
        'type': 'Cutlery',
        'have_time': True,
        'washer_running': True,
        'washer_full': True,
        'inside_dirty_dishes': False
    }
    dish_3 = {
        'name': 'launch plate',
        'type': 'Plate',
        'have_time': True,
        'washer_running': False,
        'washer_full': False,
        'inside_dirty_dishes': False
    }
    dishes = [dish_1, dish_2, dish_3]
    for dish in dishes:
        dish_instance = DishHandling(name=dish.get('name'), dish_type=dish.get('type'))
        dish_instance.have_time = dish.get('have_time')
        dish_instance.washer_running = dish.get('washer_running')
        dish_instance.washer_full = dish.get('washer_full')
        dish_instance.inside_dirty_dishes = dish.get('inside_dirty_dishes')
        dish_instance.get_dish_handling_status()
        pass
