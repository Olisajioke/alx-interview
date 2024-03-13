#!/usr/bin/python3
"""Solves the lock boxes puzzle."""


def find_keys_in_open_box(box_track):
    """Finds keys in the next open box.
    Args:
        box_track (dict): Dictionary containing the status of each box.
    Returns:
        list: Keys found in the opened box.
    """
    for box_id, details in box_track.items():
        if details['state'] == 'open':
            details['state'] = 'checked'
            return details['inside_keys']
    return None


def canUnlockAll(boxes):
    """Determines if all boxes can be opened with the keys available.
    Args:
        boxes (list): List of lists, each containing keys inside a box.
    Returns:
        bool: True if all boxes can be opened; otherwise, False.
    """
    if not boxes or len(boxes) == 1:
        return True

    trkn = {}
    while True:
        if not trkn:
            trkn[0] = {
                'state': 'open',
                'inside_keys': boxes[0],
            }
        box_keys = find_keys_in_open_box(trkn)
        if box_keys:
            for key in box_keys:
                try:
                    if trkn.get(key) and trkn[key]['state'] == 'checked':
                        continue
                    trkn[key] = {
                        'state': 'open',
                        'inside_keys': boxes[key]
                    }
                except IndexError:
                    continue
        elif 'open' in [box['state'] for box in trkn.values()]:
            continue
        elif len(trkn) == len(boxes):
            break
        else:
            return False

    return True


def main():
    """Main function to test box unlocking logic."""
    canUnlockAll([[]])


if __name__ == "__main__":
    main()
