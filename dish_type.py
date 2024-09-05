
class DishType:
    def __init__(self, dish_type):
        self._VALID_DISH_TYPES = ["Cup", "Glass", "Cutlery", "Plate", "Bowl"]
        if dish_type not in self._VALID_DISH_TYPES:
            print(f"Invalid dish type: {dish_type}")
            raise ValueError("Invalid dish type")
        self.type = dish_type
        self.place = None
        pass

    def where_to_put(self):
        if self.type in ["Cup", "Glass"]:
            self.place = 'Top rack'
        elif self.type == "Cutlery":
            self.place = 'Cutlery box'
        else:
            self.place = 'Bottom rack'
        return self.place

    pass

if __name__ == "__main__":
    sample = DishType("Cutlery")
    where = sample.where_to_put()
    print(f"belongs to {where}")