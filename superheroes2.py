hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": 5,
    "speed": 12
}
hero_1 = {
    "name": "Drasy",
    "power": "x-ray vision" ,
    "strength": 2,
    "speed": 8
}

hero_list = [hero_1, hero_0]

print("\nSuperhero ~stats\n")
for i in hero_0:
    print(f"{i}: {hero_0[i]}")
