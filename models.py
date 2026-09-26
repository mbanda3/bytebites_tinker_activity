# ByteBites backend models
#
# Classes:
# - Customer: a user of the app, identified by name and past purchase history.
# - MenuItem: a single food/drink item, with name, price, category, and popularity rating.
# - Menu: the full collection of MenuItems, filterable by category.
# - Transaction: a single order grouping the items a customer selected, computing the total cost.


class Customer:
    def __init__(self, name, purchase_history=None):
        self.name = name
        self.purchase_history = purchase_history or []


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self, items=None):
        self.items = items or []

    def filter_by_category(self, category):
        pass


class Transaction:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items or []

    def compute_total_cost(self):
        pass
