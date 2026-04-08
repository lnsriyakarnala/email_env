def grade(task, action):
    if task["id"] == "easy":
        return 1.0 if action.content == task["expected"] else 0.0

    elif task["id"] == "medium":
        score = 0
        if "complaint" in action.content:
            score += 0.5
        if "high" in action.content:
            score += 0.5
        return score

    elif task["id"] == "hard":
        score = 0
        reply = action.content.lower()
        for word in task["expected_keywords"]:
            if word in reply:
                score += 0.5
        return score

    return 0.0