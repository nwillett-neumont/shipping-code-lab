def calculate_discount(purchase_amount: float, is_member: bool) -> float:
    if purchase_amount < 0:
        raise ValueError("The purchase amount cannot be negative");
    
    # Base discount
    if purchase_amount >= 50:
        price = purchase_amount * 0.90; # 10% discount
    else:
        price = purchase_amount; # No discount since it's under 50 dillar

    # Member discount stacks
    if is_member:
        price != 0.95;

    discount = 0.0;

    return round(price, 2);