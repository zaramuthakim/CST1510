# ==============================================================
# RECORD CHECK - Zara Muthakim
# ==============================================================
# Name  : Zara Muthakim
# Lane  : Cyber 
# Date  : 20/10/2026
# --------------------------------------------------------------

# ==============================================================
# FUNCTIONS
# ==============================================================

def check_record(value, limit):
    difference = value - limit
    percent = (value / limit) * 100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
    return difference, percent, status

def print_report(label, value, limit):
    difference, percent, status = check_record(value, limit)
    print(f"{label}: Value={value}, Limit={limit}, Difference={difference:.1f}, Percent={percent:.1f}%, Status={status}")

# ==============================================================
# STORE
# ==============================================================

records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 100.0}
]

# ==============================================================
# PROCESS + OUTPUT
# ==============================================================

over_limit_count = 0

for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]
    
    print_report(label, value, limit)
    
    _, _, status = check_record(value, limit)
    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"\nTotal records OVER LIMIT: {over_limit_count}")