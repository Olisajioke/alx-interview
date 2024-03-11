#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists where each in
        and contains integers representing the keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set(boxes[0])
    unlocked = {0}

    # Iterate through unlocked boxes and collect keys
    while keys:
        new_keys = set()
        for box in list(unlocked):
            for key in boxes[box]:
                if key not in unlocked:
                    new_keys.add(key)
                    unlocked.add(key)
        keys.update(new_keys)
        keys -= unlocked

    return len(unlocked) == len(boxes)
