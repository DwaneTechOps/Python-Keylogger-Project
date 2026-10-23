from collections import Counter
from pathlib import Path

log_file = Path(__file__).with_name("First keylog save_timestamp.txt")

if not log_file.exists():
    print("Error: Log file not found.")
    print("Saved your timestamp file to your project folder.")
    raise SystemExit(1)

with log_file.open("r", encoding="utf-8") as file:
    lines = file.readlines()

events = []

for line in lines:
    if "] Key pressed: " in line:
        timestamp, key = line.strip().split(
            "] Key pressed: ", 1
        )
        events.append((timestamp.lstrip("["), key))

print("\n===== KEYBOARD LOG ANALYSIS =====")

print(f"Total events: {len(events)}")

if events:
    keys = [key for timestamp, key in events]
    key_counts = Counter(keys)

    print("\nMost frequent keys:")

    for key, count in key_counts.most_common(5):
        print(f"{key}: {count}")

    print(f"\nFirst event: {events[0][0]}")
    print(f"Last event:  {events[-1][0]}")
else:
    print("No valid keyboard events found.")

print("\n===== ANALYSIS COMPLETE =====")