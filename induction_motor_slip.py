print("========================================")
print("     INDUCTION MOTOR SLIP CALCULATOR")
print("========================================")

frequency = float(input("Enter supply frequency (Hz): "))
poles = int(input("Enter number of poles: "))
rotor_speed = float(input("Enter rotor speed (RPM): "))

if frequency <= 0:
    print("\nFrequency must be greater than zero.")
elif poles <= 0 or poles % 2 != 0:
    print("\nNumber of poles must be a positive even number.")
elif rotor_speed < 0:
    print("\nRotor speed cannot be negative.")
else:
    synchronous_speed = (120 * frequency) / poles

    if rotor_speed > synchronous_speed:
        print("\nRotor speed cannot be greater than synchronous speed.")
    else:
        slip = (synchronous_speed - rotor_speed) / synchronous_speed
        slip_percentage = slip * 100

        frequency_rotor = slip * frequency

        print("\n========== RESULTS ==========")
        print(f"Synchronous Speed = {synchronous_speed:.2f} RPM")
        print(f"Rotor Speed = {rotor_speed:.2f} RPM")
        print(f"Slip = {slip:.4f}")
        print(f"Slip Percentage = {slip_percentage:.2f}%")
        print(f"Rotor Frequency = {frequency_rotor:.2f} Hz")
        print("==============================")
