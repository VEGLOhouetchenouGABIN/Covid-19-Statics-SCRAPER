import pandas as pd



df = pd.read_csv("covid19_v4.csv")


# List of columns to delete
columns_to_delete = ['#', 'Tot\xa0Cases/1M pop', 'Deaths/1M pop', 'TotalTests',
                     'Tests/\n1M pop', '1 Caseevery X ppl', '1 Deathevery X ppl',
                     '1 Testevery X ppl', 'New Cases/1M pop', 'New Deaths/1M pop',
                     'Active Cases/1M pop']



df = df.drop(columns=columns_to_delete)


# New column names
new_column_names = {'Country,Other': 'country',
                    'TotalCases': 'totalCases',
                    'NewCases': 'newCases',
                    'TotalDeaths': 'totalDeaths',
                    'NewDeaths': 'newDeaths',
                    'TotalRecovered': 'totalRecovered',
                    'NewRecovered': 'newRecovered',
                    'ActiveCases': 'activeCases',
                    'Serious,Critical': 'seriousCritical',
                    'Population': 'population',
                    'Continent': 'continent'}

# Rename columns
df = df.rename(columns=new_column_names)

# Display updated DataFrame with new column names
print(df.head())