TINY = {
    "rows": 10,
    "cols": 10,
    "num_drones": 1,
    "max_payload": 50,
    "max_turns": 30,
    "product_weights": [10, 20, 5],
    "warehouses": [
        {"row": 0, "col": 0, "inventory": {0: 5, 1: 3, 2: 10}},
    ],
    "orders": [
        {"row": 3, "col": 3, "items": [0]},
        {"row": 5, "col": 4, "items": [1]},
    ],
}

SMALL = {
    "rows": 20,
    "cols": 20,
    "num_drones": 3,
    "max_payload": 100,
    "max_turns": 60,
    "product_weights": [10, 20, 30, 15, 5],
    "warehouses": [
        {"row": 0, "col": 0, "inventory": {0: 5, 1: 3, 2: 2, 3: 4, 4: 10}},
        {"row": 15, "col": 15, "inventory": {0: 3, 1: 5, 2: 3, 3: 2, 4: 8}},
    ],
    "orders": [
        {"row": 3, "col": 3, "items": [0, 4]},
        {"row": 10, "col": 10, "items": [1, 2]},
        {"row": 18, "col": 2, "items": [0, 3, 4]},
        {"row": 5, "col": 17, "items": [2, 1]},
        {"row": 12, "col": 8, "items": [4, 4, 4]},
    ],
}

MEDIUM = {
    "rows": 100,
    "cols": 100,
    "num_drones": 5,
    "max_payload": 200,
    "max_turns": 250,
    "product_weights": [10, 20, 30, 15, 5, 25, 40, 8, 12, 35],
    "warehouses": [
        {"row": 0, "col": 0, "inventory": {0: 10, 1: 8, 2: 5, 3: 7, 4: 20, 5: 4, 6: 3, 7: 15, 8: 10, 9: 2}},
        {"row": 50, "col": 80, "inventory": {0: 5, 1: 10, 2: 8, 3: 3, 4: 15, 5: 6, 6: 2, 7: 8, 8: 5, 9: 4}},
        {"row": 80, "col": 20, "inventory": {0: 8, 1: 5, 2: 3, 3: 10, 4: 12, 5: 8, 6: 5, 7: 6, 8: 8, 9: 3}},
    ],
    "orders": [
        {"row": 10, "col": 10, "items": [0, 1, 4]},
        {"row": 25, "col": 60, "items": [2, 5]},
        {"row": 40, "col": 30, "items": [3, 4, 7]},
        {"row": 55, "col": 55, "items": [1, 6]},
        {"row": 70, "col": 10, "items": [0, 8, 9]},
        {"row": 90, "col": 90, "items": [2, 3, 5]},
        {"row": 15, "col": 85, "items": [4, 7, 7]},
        {"row": 60, "col": 40, "items": [0, 1, 8]},
        {"row": 35, "col": 75, "items": [6, 9]},
        {"row": 85, "col": 50, "items": [3, 4, 5, 7]},
        {"row": 5, "col": 45, "items": [0, 2]},
        {"row": 45, "col": 15, "items": [1, 3, 4]},
        {"row": 75, "col": 65, "items": [5, 8, 9]},
        {"row": 20, "col": 30, "items": [7, 4]},
        {"row": 95, "col": 5, "items": [0, 6, 8]},
    ],
}
