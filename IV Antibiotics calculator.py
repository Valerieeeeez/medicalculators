import math

print("IV ANTIBIOTICS CALCULATOR")
print("=================================")

def round_up_to_nearest_ten(num):
    return math.ceil(num / 10) * 10

while True:
    print("\nEnter the values:")

    prescribed = float(input("Prescribed Medication Amount from doctor (mg): "))
    stock = float(input("Stock Medication Amount (mg per vial): "))
    volume_after_reconstitution = float(input("Volume of medication after reconstitution (ml): "))
    saline_denominator = float(input("volume of saline as per MAR (ml): "))

    # --- First calculations ---
    fraction = prescribed / stock
    amount_to_draw = volume_after_reconstitution * fraction

    # --- Display early results ---
    print("\nCALCULATED RESULTS:")
    print(f"Fraction of dose relative to stock: {fraction:.3f}")
    print(f"Amount to draw up: {amount_to_draw:.3f} ml")

    # Now get diluent input after confirming fraction
    saline_to_add = (fraction * saline_denominator) - amount_to_draw
    print(f"Saline to add: {saline_to_add}")

    # --- Continue calculations ---
    final_volume_rounded = round_up_to_nearest_ten(fraction * saline_denominator)
    infusion_rate = final_volume_rounded + 25
    concentration = prescribed / final_volume_rounded

    print(f"Final volume after dilution (rounded): {final_volume_rounded} ml")
    print(f"Infusion Rate: {infusion_rate:.3f} ml/h")
    print(f"Concentration: {concentration:.3f} mg/ml")

    again = input("\nAnother calculation? (y/n): ").lower()
    if again != 'y':
        break
