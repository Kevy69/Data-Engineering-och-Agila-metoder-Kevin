import pandas as pd
from datetime import datetime, date

print("ran")

events = {
    "summer_break": "2023-06-09 15:00",
    "lia_start": "2023-09-25 8:00",
    "christmas": "2023-12-24",
    "bellas_birthday": "2023-12-07",
    "new_year": "2024-01-01",
    "graduation_party": "2024-06-09 16:30"
}


columns = ["years", "months", "days", "hours", "minutes", "seconds"]

df = pd.DataFrame(columns=columns)

for key, value in events.items():

    date_string = value
    date_format = "%Y-%m-%d"

    try:
        target_date = datetime.strptime(date_string, date_format + " %H:%M")
    except ValueError:
        target_date = datetime.strptime(date_string, date_format).date()

    today = date.today()

    if isinstance(target_date, datetime):
        time_diff = target_date - datetime.combine(today, datetime.min.time())
    else:
        time_diff = target_date - today

    years = time_diff.days // 365
    months = time_diff.days // 30
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds // 60) % 60
    seconds = time_diff.seconds % 60

    time_diff_list = [str(years), str(months), str(days), str(hours), str(minutes), str(seconds)]

    # Adding the first row with index 'a'
    df.loc[key] = time_diff_list
    
    
with open("countdown.log", "a") as f:
    f.write(df.to_markdown())


