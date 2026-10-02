"""
RECORD CHECK  -  my version
===========================

Name  : Zara Muthakim
Lane  : Cybersecurity
Date  : 25/09/2026

Run it:   python template.py
"""

# ==================================================================== INPUT
label = input("Enter a name, hostname, or IP: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))


# ================================================================== PROCESS
difference = second - first
percent = (first / second) * 100


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  Label:       {label}")
print(f"  First:       {first:>10.2f}")
print(f"  Second:      {second:>10.2f}")
print(f"  Difference:  {difference:>+10.2f}")
print(f"  Percent:     {percent:>10.2f}%")
print("  Check complete.")

print("=" * 34)