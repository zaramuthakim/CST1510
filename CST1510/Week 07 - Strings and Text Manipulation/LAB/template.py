"""
RECORD CHECK  -  my version
===========================

Name  : Zara muthakim
Lane  : Cyber
Date  : 08/11/2026

Run it:  python template.py
"""

def parse_line(raw_line):
    """Cleans a messy string and parses it into a dictionary."""
    cleaned = raw_line.strip()
    
    if not cleaned:
        return {}
        
    parts = cleaned.split(",")
    data = {}
    
    data["name"] = parts[0].strip()
    
    for part in parts[1:]:
        if "=" in part:
            key, value = part.split("=", 1)
            data[key.strip().lower()] = value.strip()
            
    return data

def status_of(record):
    """Returns FLAGGED if an attack was successful, otherwise OK."""
    result = record.get("result", "").upper()
    if result == "FAILED":
        return "FLAGGED"
    return "OK"

raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    "  Srv-01 , used=87 , total=100  ",
    "   src=192.168.1.1, attempts=1 , result=success   ",
    "Srv-99, used=0, total=500"
]

flagged_count = 0

for raw_record in raw_records:
    if not raw_record.strip():
        continue
        
    parsed_record = parse_line(raw_record)
    status = status_of(parsed_record)
    
    print(f"Parsed: {parsed_record}")
    print(f"Status: {status}\n")
    
    if status == "FLAGGED":
        flagged_count += 1

print(f"--- SUMMARY ---")
print(f"Total records processed: {len(raw_records)}")
print(f"Total flagged: {flagged_count}")