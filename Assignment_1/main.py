from basic_lfsr import BasicLFSR
from general_lfsr import GeneralLFSR

# Basic LFSR
basic_lfsr = BasicLFSR('0110')
print("Basic LFSR Output:")
for _ in range(20):
    print(f"Current State: {basic_lfsr.get_current_state()}, Next Bit: {basic_lfsr.next_bit()}")

# General LFSR
general_lfsr = GeneralLFSR('0110', [0, 1])  # Example taps
print("\nGeneral LFSR Output:")
for _ in range(20):
    print(f"Current State: {general_lfsr.get_current_state()}, Next Bit: {general_lfsr.next_bit()}")