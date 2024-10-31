def calculate_energy_from_mass(m):
    return int(m) * (300000000 **2)

def main():
    m = input("Enter the mass value: ")
    e = calculate_energy_from_mass(m)
    print(f"E: {e}")

main()