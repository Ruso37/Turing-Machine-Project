
import random
import time

# Simulated Turing Machine Runner for Halting Problem demo

def simulate_tm_execution(tm_description, input_string):
    print(f"Simulating TM: {tm_description} with input: {input_string}")
    
    # Simulated behavior
    print("Running...")
    time.sleep(1)
    
    # Fake a halting decision
    halts = random.choice([True, False])

    if halts:
        print("✅ This Turing Machine HALTS on the given input.")
    else:
        print("❌ This Turing Machine DOES NOT HALT on the given input.")
        print("(Simulation stopped due to potential infinite loop)")

# User interaction
if __name__ == "__main__":
    print("=== Halting Problem Simulator ===")
    desc = input("Enter a description of the Turing Machine: ")
    user_input = input("Enter the input string: ")
    simulate_tm_execution(desc, user_input)
