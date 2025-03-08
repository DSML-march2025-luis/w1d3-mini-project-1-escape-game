# 
# Data validation tests:
# 
# - Setup: pip install pytest
# - Run the tests: pytest rooms_test.py
# 
# 

import pytest
from rooms import rooms

def test_room_structure():
    """Ensure each room follows the expected data structure."""
    for room_name, room_data in rooms.items():
        assert "interactive_items" in room_data, f"Missing 'interactive_items' in {room_name}"
        assert "doors" in room_data, f"Missing 'doors' in {room_name}"
        assert isinstance(room_data["interactive_items"], list), f"'interactive_items' must be a list in {room_name}"
        assert isinstance(room_data["doors"], list), f"'doors' must be a list in {room_name}"

def test_interactive_items_structure():
    """Ensure interactive_items follows the expected data structure."""
    for room_name, room_data in rooms.items():
        for item in room_data["interactive_items"]:
            assert "item_name" in item, f"Missing 'item_name' in one of the items of {room_name}"
            assert "keys_to_collect" in item, f"Missing 'keys_to_collect' in one of the items of {room_name}"
            assert isinstance(item["item_name"], str), f"'item_name' must be a string in one of the items of {room_name}"
            assert isinstance(item["keys_to_collect"], list), f"'keys_to_collect' must be a list in one of the items of {room_name}"

def test_doors_structure():
    """Ensure doors follows the expected data structure."""
    for room_name, room_data in rooms.items():
        for doors in room_data["doors"]:
            assert "door_name" in doors, f"Missing 'door_name' in one of the doors of {room_name}"
            assert "destination" in doors, f"Missing 'destination' in one of the doors of {room_name}"
            assert isinstance(doors["door_name"], str), f"'door_name' must be a string in one of the doors of {room_name}"
            assert isinstance(doors["destination"], str), f"'destination' must be a string in one of the doors of {room_name}"


def test_keys_to_collect_are_valid():
    """Ensure all keys_to_collect open an existing door."""

    # Gather all door names into a set for fast lookup
    valid_doors = {door["door_name"] for room in rooms.values() for door in room["doors"]}

    # Check that each key in keys_to_collect points to a valid door name
    for room in rooms.values():
        for item in room["interactive_items"]:
            for key in item["keys_to_collect"]:
                assert key in valid_doors, f"Invalid door name {key} in {item['item_name']}"


def test_doors_are_valid():
    """Ensure all doors lead to a valid room OR to the outside."""

    # Gather all room names into a set for fast lookup
    valid_rooms = set(rooms.keys())

    # Check that each destination in a door points to a valid room name
    for room_name, room_data in rooms.items():
        for door in room_data["doors"]:
            assert door["destination"] in valid_rooms | {"Outside"} , f"Invalid room name {door["destination"]} in {room_name} / {door["door_name"]}"


