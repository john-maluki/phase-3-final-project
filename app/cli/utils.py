def print_facilities(facilities):
    print("\n-" * 3 + " Listing all facilities" + "-" * 50)
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for facility in facilities:
        print(" " * 5 + f" {facility.id}" + " " * 5 + f"{facility.name}" + " " * 5)
