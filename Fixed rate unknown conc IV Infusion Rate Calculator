print("IV INFUSION MCG/KG/H RATE CALCULATOR")
print("=================================")

while True:
    print("\nEnter the values:")
    prescribed = float(input("Prescribed Medicine Amount (mcg): "))
    volume = float(input("Medicine Volume (ml): "))
    stock = float(input("Stock Strength (mcg/ml): "))
    rate = float(input("Rate (ml/h): "))
    weight = float(input("Patient Weight (kg): "))
    
    concentration = prescribed / volume
    conc_rate = concentration * rate
    infusion_mcg = conc_rate / weight
    infusion_mg = infusion_mcg / 1000
    
    print("\nRESULTS:")
    print(f"Concentration: {concentration:.5f} mcg/ml")
    print(f"Concentration Rate: {conc_rate:.5f} mcg/h")
    print(f"Infusion Rate: {infusion_mcg:.5f} mcg/kg/h")
    print(f"Infusion Rate: {infusion_mg:.5f} mg/kg/h")
    
    again = input("\nAnother calculation? (y/n): ").lower()
    if again != 'y':
        break
