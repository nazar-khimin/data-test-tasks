class Pizza:
    __order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.__order_number += 1
        self.order_number = Pizza.__order_number

    @staticmethod
    @classmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])



# Examples:
p1 = Pizza(["bacon", "parmesan", "ham"]) # order 1
p2 = Pizza.garden_feast()

print(f'{p1.ingredients} \n {p2.ingredients} \n {p1.order_number} \n {p2.order_number}')