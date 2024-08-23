class DishHandling:
    def __init__(self, name):
        self.name = name
        self.have_time = True
        self.washer_running = False
        self.washer_full = False
        self.inside_dirty_dishes = False

        pass

    def put_clean_dished_in_cupboard(self):
        print(' Put clean dishes in cupboard')
        pass

    def turn_on_washer(self):
        print(' Turn on dish washer')
        pass

    def hand_wash_dishes(self):
        print(' Hand wash your {}.'.format(self.name))
        pass

    def place_dished_in_washer(self):
        print(' Place {} in dish washer'.format(self.name))
        pass

    def keep_dishes_with_yourself(self):
        print(' Bring back your {} to your desk and NOT put it in sink'.format(self.name))
        pass

    def get_dish_handling_status(self):
        if self.have_time is False:
            self.keep_dishes_with_yourself()
            pass
        else:
            if self.washer_running is False:
                if self.washer_full is False:
                    self.place_dished_in_washer()
                else:
                    if self.inside_dirty_dishes is False:
                        self.put_clean_dished_in_cupboard()
                        self.place_dished_in_washer()
                    else:
                        self.turn_on_washer()
                        self.hand_wash_dishes()
                        pass
                    pass
                pass
            else:
                self.hand_wash_dishes()
                pass

    pass
