"""For loops syntax and practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for pet in pets:
    print(f"Good boy, {pet}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
