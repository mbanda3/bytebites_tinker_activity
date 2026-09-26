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
        # Return only the items whose category matches (case-insensitive).
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self, descending=True):
        # Return items ordered by popularity_rating, most popular first by default.
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=descending)


class Transaction:
    def __init__(self, selected_items=None):
        self.selected_items = selected_items or []

    def compute_total_cost(self):
        # Sum the price of every selected item.
        return sum(item.price for item in self.selected_items)


if __name__ == "__main__":
    # Manual test scenario: create sample objects and exercise each method.
    burger = MenuItem("Spicy Burger", 8.99, "Entrees", popularity_rating=4.5)
    soda = MenuItem("Large Soda", 2.49, "Drinks", popularity_rating=3.0)
    fries = MenuItem("Curly Fries", 3.99, "Sides", popularity_rating=4.8)
    shake = MenuItem("Chocolate Shake", 4.99, "Drinks", popularity_rating=4.2)

    menu = Menu([burger, soda, fries, shake])
    print("All items:", [item.name for item in menu.items])

    drinks = menu.filter_by_category("Drinks")
    print("Drinks:", [item.name for item in drinks])
    assert [item.name for item in drinks] == ["Large Soda", "Chocolate Shake"]

    most_popular_first = menu.sort_by_popularity()
    print("Sorted by popularity:", [item.name for item in most_popular_first])
    assert most_popular_first[0].name == "Curly Fries"

    alice = Customer("Alice", purchase_history=["Spicy Burger"])
    order = Transaction([burger, fries, soda])
    total = order.compute_total_cost()
    print(f"{alice.name}'s total cost:", total)
    assert round(total, 2) == round(8.99 + 3.99 + 2.49, 2)

    print("All manual checks passed.")
