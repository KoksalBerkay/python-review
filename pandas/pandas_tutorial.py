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

titanic = pd.read_csv("pandas/data/titanic.csv")
print(titanic) # The first and last 5 rows will be shown by default.

# The first n rows of a pandas DataFrame.
print(titanic.head(8)) # n = 8
# The last n rows of a pandas DataFrame.
print(titanic.tail(7)) # n = 7

print(titanic.dtypes)

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")


titanic = pd.read_csv("pandas/data/titanic.csv")
ages = titanic["Age"]
print(ages.head())
print(ages.shape)

age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
print(age_sex.shape)

# To select rows based on a conditional expression,
# use a condition inside the selection brackets []
above_35 = titanic[titanic["Age"] > 35]
print(above_35.head())
print(above_35.shape)

# the isin() conditional function returns a True for each row the values are in the provided list.
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
# checks for which rows the Pclass column is either 2 or 3.
print(class_23.head())

class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
print(class_23.head())

# The notna() conditional function returns a True for each row the values are not an Null value.
# As such, this can be combined with the selection brackets [] to filter the data table.
age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na.head())
print(age_no_na.shape)

# Names of passengers older than 35 years.
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print(adult_names.head())

# The rows 10 till 25 and columns 3 to 5.
print(titanic.iloc[9:25, 2:5])

# When selecting specific rows and/or columns with loc or iloc, new values can be assigned to the selected data.
titanic.iloc[0:3, 3] = "anonymous"
print(titanic)