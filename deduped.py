def deduped(items):
    """Return new list from items with duplicates removed."""

    new_items = []

    for item in items:
        if item not in new_items:
            new_items.append(item)

    return new_items