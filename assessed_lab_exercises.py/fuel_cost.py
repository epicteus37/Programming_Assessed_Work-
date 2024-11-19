def fuel_cost(distance_miles):
     MPG = 50  # Miles per gallon
     LITRES_PER_GALLON = 4.5
     PRICE_PER_LITRE = 1.49  # Price in pounds per liter
     gallons_needed = distance_miles / MPG
     litres_needed = gallons_needed * LITRES_PER_GALLON
     total_cost = litres_needed * PRICE_PER_LITRE
     return total_cost
# distance = 50
# cost = fuel_cost(distance)
# print(f"Total fuel price = £{cost:.2f}")
