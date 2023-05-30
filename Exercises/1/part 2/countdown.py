import pandas as pd
from datetime import datetime




# date_string = "2023-06-09 15:00"
# date_format = "%Y-%m-%d %H:%M"
# parsed_date = datetime.strptime(date_string, date_format)

# year = parsed_date.year
# month = parsed_date.month
# day = parsed_date.day
# hour = parsed_date.hour
# minute = parsed_date.minute
# second = parsed_date.second




# with open("countdown.log", "a") as f:
#     f.write("")


# df = pd.DataFrame()

# df["Saanvi"] = [96, 90]

# print(df.to_markdown())



df = pd.DataFrame(
    data={
        "years": ["x", "x", "x", "x", "x", "x"],
        "months": ["x", "x", "x", "x", "x", "x"],
        "days": ["x", "x", "x", "x", "x", "x"],
        "hours": ["x", "x", "x", "x", "x", "x"],
        "minutes": ["x", "x", "x", "x", "x", "x"],
        "seconds": ["x", "x", "x", "x", "x", "x"]
    },
    index=[
        "summer_break",
        "lia_start",
        "christmas",
        "bellas_birthday",
        "new_year",
        "graduation_party"
    ]
)

print(df.to_markdown())




