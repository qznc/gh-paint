import subprocess

COMMIT_COUNTER = 1

def create_commit(date):
    global COMMIT_COUNTER
    commit_date = date.strftime("%Y-%m-%d %H:%M:%S")
    with open("dummy.txt", "w") as fh:
        fh.write(f"{COMMIT_COUNTER}\n")
        COMMIT_COUNTER += 1
    subprocess.run(['git', 'commit', '-m', f'Commit for {date}', '--date', commit_date])

width = 52
height = 7

header_data = (
    "````````````>H:W%2%2%2%2%2%2%2%2%2%2%2%2%2%2%2%2%2%2```````"
    "%2%2%2%2%2%2````````````````````%2%2%2%2%2%2%2%2%2%2%2%2%2%2%2%2"
    "%2%2%2%2%2%2`````````````````````"
    "%2%2%2%2%2%2%2%2````%2%20$Q]```"
    "%2%20$Q]%2%2````%2%2%2%2%2%2%2%2%2%2```"
    "%2%2%2%2%2%2%2%2%2%2%2%2%2%2````%2%2%2%2%2%2%2%2%2%2```"
    "````%2%2%2%2%2%2```````%2%2%2%2```````>H:W"
    "%2%2```````>H:W%2%2````````````%2%2%2%2%2%2%2%2```````"
    "%2%2```````%2%2`````````````````````"
    "%2%2````%2%2%2%2```````````````````"
    "%2%2```````%2%2````````0$Q]```````%2%2%2%2%2%2%2%2"
    "%2%2`````````````%2%2```````%2%2%2%2%2%2```"
    "%2%2%2%2%2%2%2%2%2%2````%2%2%2%2````````>H:W%2%2```````%2%2"
    "```````%2%2```````%2%2```````%2%2%2%2```"
    "%2%2%2%2%2%2%2%2%2%2````%2%2```````%2%2```"
    "HJ[?0$Q]%2%2````%2%2%2%2%2%2%2%2%2%2```````%2%2```"
    "````%2%2HJ[?HJ[?```````%2%2```````%2%2```"
    "````%2%2%2%2```````%2%2```````"
    "%2%2```````0$Q]%2%2```````%2%2%2%2"
    "```````%2%2```````````````````>H:W%2%2>H:W```"
    "%2%2````%2%2%2%2```````%2%2%2%2%2%2%2%2%2%2```````"
    "%2%2%2%2%2%2>H:W`````````````%2%2%2%2%2%2%2%2"
    "%2%2```````%2%2```````%2%2````````"
)

with open("gh.data", "br") as fh:
    data = fh.read()

for y in range(height):
    for x in range(width):
        pixel = data[y*width + x]
        print(f"{pixel:x} ", end="")
    print()

from datetime import datetime, timedelta

def date_range_past_year():
    today = datetime.now().date()
    start_date = today - timedelta(days=52*7)
    
    current_date = start_date
    while current_date <= today:
        yield current_date
        current_date += timedelta(days=1)

def handle_date(i, date):
    x = i // 7
    y = i % 7
    pixel = data[y*width + x]
    for i in range(pixel):
        create_commit(date)

print()
i = -1
for date in date_range_past_year():
    if i >= 0 or date.isoweekday() == 7:
        i += 1
        handle_date(i, date)
