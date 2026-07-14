def apply_discount_batch(items, discount_percent, min_price=0):
    if not (0 <= discount_percent <= 100):
        raise ValueError("discount_percent must be between 0 and 100")

    results = []
    for item in items:
        if item["price"] < min_price:
            continue
        results.append({
            "name": item["name"],
            "price": item["price"] * (1 - discount_percent / 100),
        })
    return results
