"""Dictionary practice"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

ice_cream["vanilla"] += 110

print(len(ice_cream))  # Print 3

ice_cream["mint"] = 3  # append to dict

print(ice_cream["chocolate"])  # print 12 which is value

has_pbj: bool = "pbj" in ice_cream  # False, checks if key in dict

ice_cream.pop("strawberry")  # return 4, remove that value

# Loops over keys
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
