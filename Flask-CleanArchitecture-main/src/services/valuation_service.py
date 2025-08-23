def estimate_diamond_price(carat, color, clarity):
    # Ví dụ công thức rất đơn giản (bạn có thể cải tiến sau)
    base_price = 5000
    price = base_price * carat

    if color == "D":
        price *= 1.2
    if clarity == "VVS1":
        price *= 1.3

    return round(price, 2)
