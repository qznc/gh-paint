import subprocess
from datetime import datetime, timedelta

COMMIT_COUNTER = 1
FILENAME = "dummy.txt"
BRANCH = "gh-paint"
YEAR = 2024
width = 52
height = 7
with open("gh.data", "br") as fh:
    data = fh.read()


def run(cmd):
    print(cmd)
    cp = subprocess.run(cmd, check=True, capture_output=True)


def create_commit(date):
    global COMMIT_COUNTER
    commit_date = date.strftime("%Y-%m-%d %H:%M:%S")
    with open("dummy.txt", "w") as fh:
        fh.write(f"{COMMIT_COUNTER}\n")
        COMMIT_COUNTER += 1
    run(["git", "add", FILENAME])
    run(["git", "commit", "-m", f"Commit for {date}", "--date", commit_date])


def commit_dates():
    current_year = datetime.now().year
    first_day_of_last_year = datetime(current_year - 1, 1, 1)
    cur = first_day_of_last_year
    while cur.year < current_year:
        yield cur
        cur += timedelta(days=1)


def do_date(i, date):
    x = i // 7
    y = i % 7
    pixel = data[y * width + x] // 16
    for i in range(pixel):
        create_commit(date)


run(["git", "checkout", "-b", BRANCH])
i = -1
for date in commit_dates():
    if i >= 0 or date.isoweekday() == 7:
        i += 1
        do_date(i, date)
        # break # DEV
