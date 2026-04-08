TASKS = [
    {
        "id": "easy",
        "email": "I want a refund for my order",
        "expected": "refund_request"
    },
    {
        "id": "medium",
        "email": "My product is broken and I need urgent help",
        "expected": {
            "type": "complaint",
            "priority": "high"
        }
    },
    {
        "id": "hard",
        "email": "I was charged twice. Please help.",
        "expected_keywords": ["sorry", "refund"]
    }
]