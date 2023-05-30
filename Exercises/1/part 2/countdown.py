import pandas as pd


events = {
    "summer_break": "2023-06-09 15:00",
    "lia_start": "2023-09-25 8:00",
    "christmas": "2023-12-24",
    "bellas_birthday": "2023-12-07",
    "new_year": "2024-01-01",
    "graduation_party": "2024-06-09 16:30"
}


with open("countdown.log", "a") as f:
    f.write("")
    

df = pd.DataFrame(
    data={"years": ["elk", "pig"],
          "months": ["dog", "quetzal"],
          "days": ["dog", "quetzal"],
          "hours": ["dog", "quetzal"],
          "minutes": ["dog", "quetzal"],
          "seconds": ["dog", "quetzal"]
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