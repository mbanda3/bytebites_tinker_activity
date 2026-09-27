from models import MenuItem, Menu, Transaction


def make_sample_items():
    return [
        MenuItem("Spicy Burger", 8.99, "Entrees", popularity_rating=4.5),
        MenuItem("Large Soda", 2.49, "Drinks", popularity_rating=3.0),
        MenuItem("Curly Fries", 3.99, "Sides", popularity_rating=4.8),
        MenuItem("Chocolate Shake", 4.99, "Drinks", popularity_rating=4.2),
    ]


def test_calculate_total_with_multiple_items():
    # A $10 burger and a $5 soda should total $15.
    burger = MenuItem("Burger", 10.00, "Entrees", popularity_rating=4.0)
    soda = MenuItem("Soda", 5.00, "Drinks", popularity_rating=3.0)
    order = Transaction([burger, soda])

    assert order.compute_total_cost() == 15.00


def test_order_total_is_zero_when_empty():
    # An order with nothing selected should return 0, not crash.
    order = Transaction()

    assert order.compute_total_cost() == 0


def test_filter_by_category_returns_only_matching_items():
    # Filtering "Drinks" should only return liquid items.
    menu = Menu(make_sample_items())

    drinks = menu.filter_by_category("Drinks")

    assert [item.name for item in drinks] == ["Large Soda", "Chocolate Shake"]


def test_filter_by_category_is_case_insensitive():
    menu = Menu(make_sample_items())

    drinks = menu.filter_by_category("drinks")

    assert [item.name for item in drinks] == ["Large Soda", "Chocolate Shake"]


def test_filter_by_category_returns_empty_list_when_no_match():
    menu = Menu(make_sample_items())

    desserts = menu.filter_by_category("Desserts")

    assert desserts == []


def test_sort_by_popularity_orders_most_popular_first():
    menu = Menu(make_sample_items())

    ranked = menu.sort_by_popularity()

    assert [item.name for item in ranked] == [
        "Curly Fries",
        "Spicy Burger",
        "Chocolate Shake",
        "Large Soda",
    ]
