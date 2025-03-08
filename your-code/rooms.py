
rooms = {
    "Game Room": {
        "interactive_items": [
            {
                "item_name": "Couch",
                "keys_to_collect": []
            },
            {
                "item_name": "Piano",
                "keys_to_collect": ["Door A"]
            }
        ],
        "doors": [
            {
                "door_name": "Door A",
                "destination": "Bedroom 1"
            }
        ],
    },
    "Bedroom 1": {
        "interactive_items": [
            {
                "item_name": "Queen Bed",
                "keys_to_collect": ["Door B"]
            }
        ],
        "doors": [
            {
                "door_name": "Door A",
                "destination": "Game Room"
            },
            {
                "door_name": "Door B",
                "destination": "Bedroom 2"
            },
            {
                "door_name": "Door C",
                "destination": "Living Room"
            }
        ],
    },
    "Bedroom 2": {
        "interactive_items": [
            {
                "item_name": "Double Bed",
                "keys_to_collect": ["Door C"]
            },
            {
                "item_name": "Dresser",
                "keys_to_collect": ["Door D"]
            }
        ],
        "doors": [
            {
                "door_name": "Door B",
                "destination": "Bedroom 1"
            }
        ],
    },
    "Living Room": {
        "interactive_items": [
            {
                "item_name": "Dining Table",
                "keys_to_collect": []
            }
        ],
        "doors": [
            {
                "door_name": "Door D",
                "destination": "Outside"
            }
        ],
    },
}