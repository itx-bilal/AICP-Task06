CEMENT_WEIGHT_LOWER = 24.9
CEMENT_WEIGHT_UPPER = 25.1
GRAVEL_SAND_WEIGHT_LOWER = 49.9
GRAVEL_SAND_WEIGHT_UPPER = 50.1
CEMENT_PRICE = 3
GRAVEL_PRICE = 2
SAND_PRICE = 2
SPECIAL_PACK_CEMENT = 1
SPECIAL_PACK_SAND = 2
SPECIAL_PACK_GRAVEL = 2
SPECIAL_PACK_PRICE = 10

def check_single_sack():
    print("Enter details for a single sack:")
    contents = input("Enter contents (C for cement, G for gravel, S for sand): ").upper()
    weight = float(input("Enter weight in kilograms: "))

    if contents not in ['C', 'G', 'S']:
        print("Error: Invalid contents. Please enter C, G, or S.")
        return False

    if contents == 'C' and not (CEMENT_WEIGHT_LOWER < weight < CEMENT_WEIGHT_UPPER):
        print("Error: Invalid weight for cement sack.")
        return False
    elif contents in ['G', 'S'] and not (GRAVEL_SAND_WEIGHT_LOWER < weight < GRAVEL_SAND_WEIGHT_UPPER):
        print(f"Error: Invalid weight for {contents.lower()} sack.")
        return False

    print("Sack accepted:")
    print(f"Contents: {contents}")
    print(f"Weight: {weight} kilograms")
    return True

def check_customer_order():
    total_weight = 0
    total_rejected = 0

    num_cement = int(input("Enter the number of cement sacks required: "))
    num_gravel = int(input("Enter the number of gravel sacks required: "))
    num_sand = int(input("Enter the number of sand sacks required: "))

    for _ in range(num_cement):
        if not check_single_sack():
            total_rejected += 1
        else:
            total_weight += CEMENT_WEIGHT_LOWER

    for _ in range(num_gravel):
        if not check_single_sack():
            total_rejected += 1
        else:
            total_weight += GRAVEL_SAND_WEIGHT_LOWER

    for _ in range(num_sand):
        if not check_single_sack():
            total_rejected += 1
        else:
            total_weight += GRAVEL_SAND_WEIGHT_LOWER

    return total_weight, total_rejected

def calculate_order_price(total_weight, total_rejected):
    regular_price = (CEMENT_PRICE * total_weight) + (GRAVEL_PRICE * total_weight) + (SAND_PRICE * total_weight)

    num_special_packs = min(
        total_weight // (SPECIAL_PACK_CEMENT + SPECIAL_PACK_SAND + SPECIAL_PACK_GRAVEL),
        total_rejected // (SPECIAL_PACK_CEMENT + SPECIAL_PACK_SAND + SPECIAL_PACK_GRAVEL)
    )

    special_packs_price = num_special_packs * SPECIAL_PACK_PRICE
    discount_price = regular_price - special_packs_price

    if num_special_packs > 0:
        print(f"\nSpecial Packs Applied: {num_special_packs}")
        print(f"Regular Price: ${regular_price}")
        print(f"Discounted Price: ${discount_price}")
        print(f"Amount Saved: ${regular_price - discount_price}")
    else:
        print(f"\nRegular Price: ${regular_price}")

total_weight, total_rejected = check_customer_order()
calculate_order_price(total_weight, total_rejected)
