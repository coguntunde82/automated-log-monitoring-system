import time

log_file = "sample_logs.txt"
failed_attempts = 0

print("Starting Automated Log Monitoring System...")

with open(log_file, "r") as file:
    for line in file:
        print("Reading:", line.strip())

        if "failed login" in line.lower():
            failed_attempts += 1

        if failed_attempts >= 3:
            print("ALERT: Multiple failed login attempts detected.")
            break

print("Monitoring complete.")
