import csv
from pathlib import Path

HISTORY_FILE = Path("logs/post_log.csv")

def is_posted(title):
    if not HISTORY_FILE.exists():
        return False
    with open(HISTORY_FILE, newline='') as f:
        return title in [row[0] for row in csv.reader(f)]

def record_post(title):
    with open(HISTORY_FILE, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([title])
