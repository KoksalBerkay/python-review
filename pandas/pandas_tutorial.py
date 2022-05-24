import pandas as pd
# DataFrame is a 2-dimensional data structure that
# can store data of different types in columns.
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr.William Henry",
            "Bonnell, Miss. Elizabeth,"
        ],
        "Age": [22, 35 ,58],
        "Sex": ["male", "male", "female"],
    }
)

# Each column in a DataFrame is a Series
# A Series does have row labels.
ages = pd.Series([22, 35, 58], name="Age")

print(df["Age"].max())
print(ages.max())

# The describe() method provides a quick overview
# of the numerical data in a DataFrame.
print(df.describe())