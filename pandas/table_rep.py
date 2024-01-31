import pandas as pd 

df = pd.DataFrame(
    {
        "Name":[
            "Rishabh",
            "Pulkit",
            "Virat Kohli"
        ],
        "Age": [18, 20, 35],
        "Gender": ["Male", "Gay", "King"]
    }
)

# print(df)

print(df.head(1))