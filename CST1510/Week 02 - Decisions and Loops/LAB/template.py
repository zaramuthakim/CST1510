"""
==================================
RECORD CHECK  -  my version
==================================

Name  : Zara Muthakim
Lane  : Cyber Security
Date  : 02/10/2026

Run it:  python template.py
"""

# ==========================================
# Cyber Security Lane - Excellent Level
# ==========================================

over_limit_count = 0

print("==================================")

while True:
    #three inputs
    source_ip = input("Enter source IP (or 'quit' to finish): ")
    
    #if the user wants to stop
    if source_ip.lower() == "quit":
        break
        
    failed_logins = int(input("Enter failed logins: "))
    total_attempts = int(input("Enter total attempts: "))
    
    # calculate the missing values
    # difference (successful attempts)
    successful_attempts = total_attempts - failed_logins
    
    # percentage (failed login rate)
    # Rules: Do not type any number you could calculate. We calculate it here.
    percent = (failed_logins / total_attempts) * 100
    
    # the status using if / elif / else for a 3-tier status
    if percent >= 100:
        status = "OVER LIMIT"
        # how many records came back OVER LIMIT during the session
        over_limit_count += 1  
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
        
    # print the bordered report
    # Rules: All numbers show 2 decimal places and are right-aligned so they line up.
    print("\n==================================")
    print(f" RECORD CHECK  -  {source_ip}")
    print("==================================")
    # >8.2f right-aligns the number to 8 spaces and gives 2 decimal places
    print(f" Failed Logins : {failed_logins:>8.2f}")
    print(f" Total Attempts: {total_attempts:>8.2f}")
    print(f" Successful    : {successful_attempts:>8.2f}")
    print(f" Percent       : {percent:>8.2f} %")
    print(f" Status        : {status:>8}")
    print("==================================\n")

# the loop ends, print the total count once
print("==================================")
print(f"Total OVER LIMIT records: {over_limit_count}")
print("==================================")
