
def player(prev_play, opponent_history=[]):

    if prev_play == "":
        opponent_history.clear()
        return "S"

    opponent_history.append(prev_play)

    pattern_length = 4

    if len(opponent_history) <= pattern_length:
        return "R"

    pattern = "".join(opponent_history[-pattern_length:])
    predictions = []

    for i in range(len(opponent_history) - pattern_length):
        old_pattern = "".join(
            opponent_history[i:i + pattern_length]
        )

        if old_pattern == pattern:
            predictions.append(
                opponent_history[i + pattern_length]
            )

    if predictions:
        predicted = max(
            set(predictions),
            key=predictions.count
        )
    else:
        pattern_length = 3
        pattern = "".join(opponent_history[-pattern_length:])
        predictions = []

        for i in range(len(opponent_history) - pattern_length):
            old_pattern = "".join(
                opponent_history[i:i + pattern_length]
            )

            if old_pattern == pattern:
                predictions.append(
                    opponent_history[i + pattern_length]
                )

        if predictions:
            predicted = max(
                set(predictions),
                key=predictions.count
            )
        else:
            predicted = opponent_history[-1]

    if predicted == "R":
        return "P"
    elif predicted == "P":
        return "S"
    else:
        return "R"
