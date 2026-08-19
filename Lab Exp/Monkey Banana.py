# Monkey and Banana Problem Simulation

def monkey_banana():
    print("Initial State:")
    print("Monkey is on the floor.")
    print("Box is away from the banana.")
    print("Banana is hanging above.\n")

    actions = [
        "1. Monkey moves to the box.",
        "2. Monkey pushes the box under the banana.",
        "3. Monkey climbs onto the box.",
        "4. Monkey reaches for the banana.",
        "5. Monkey grabs the banana."
    ]

    print("Optimal Action Plan:")
    for action in actions:
        print(action)

    print("\nGoal Achieved: Monkey has the banana!")

# Run the simulation
monkey_banana()
