def display_weights(name: str, earth_weight: float) -> None:
    """
    Calculate and display the weight on planets based on the Users Earth weight.

    :param name: User's name
    :param earth_weight: Weight on Earth
    """
    # Surface Gravity Factors
    GRAVITY_FACTORS = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066
    }

    print(f"\n{name}, here are your weights on our Solar System's Planets:")
    for planet, gravity in GRAVITY_FACTORS.items():
        planet_weight = earth_weight * gravity
        print(f"Weight on {planet}: {planet_weight:10.2f}")


# Welcome message and input
print("Welcome to Interplanetary Weight Calculator!")
name = input("What is your name: ")
earth_weight = float(input("What is your weight: "))

# Calculation and display
display_weights(name, earth_weight)