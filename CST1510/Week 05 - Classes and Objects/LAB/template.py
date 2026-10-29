NAME = Zara Muthakim
LANE = Cyber
DATE = 27/10/2026
print(f"Name: {NAME}")
print(f"Lane: {LANE}")
print(f"Date: {DATE}")
print("-" * 34)

# ==================================================
# 1. Define a class called Record.
# ==================================================

class Record:
    def __init__(self, label, value, limit):
        """Initialise a record with label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT, WARNING, or OK based on value/limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

    def over_limit_count(self):
        """Return 1 if over limit, else 0 for running totals."""
        return 1 if self.status() == "OVER LIMIT" else 0

# ==================================================
# 2. Create your records.
# ==================================================

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 95.0, 100.0),
    Record("R-004", 45.0, 100.0),
    Record("R-005", 100.0, 100.0)
]

# ==================================================
# 3. Print a report for each record.
# ==================================================

total_over_limit = 0

for record in records:
    print()
    print("*" * 34)
    print(f"* RECORD CHECK - {record.label:<17}*")
    print("*" * 34)
    
    print(f"Label:  {record.label}")
    print(f"Value:  {record.value}")
    print(f"Limit:  {record.limit}")
    print(f"Status: {record.status()}")
    
    total_over_limit += record.over_limit_count()
    
    print("*" * 34)

print(f"\nTotal records OVER LIMIT: {total_over_limit}")