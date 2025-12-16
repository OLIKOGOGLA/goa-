def greetings(special, *guests, **visitors):
    # 1) 
    print(f"Welcome {special}")
    print("-" * 30)

    # 2) 
    for guest in guests:
        print(f"Hello {guest}")

    print("-" * 30)

    # 3) 
    for key, value in visitors.items():
        print(f"{key}: {value}")
