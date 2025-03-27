## Methods For Filtering Rows and Removing Column

```python
# Method 1: Boolean indexing + drop
df = df[df['Functioning Day'] == 'Yes']  # Filter rows where business is open
df = df.drop('Functioning Day', axis=1)  # Remove the column using drop method

# Method 2: query() method + drop columns parameter
df = df.query("Functioning Day == 'Yes'")  # Filter using query method
df = df.drop(columns=['Functioning Day'])  # Remove column using columns parameter

# Method 3: loc indexer + del statement
df = df.loc[df['Functioning Day'] == 'Yes']  # Filter using loc accessor
del df['Functioning Day']  # Remove column using Python's del keyword

# Method 4: Chained operations
df = df[df['Functioning Day'] == 'Yes'].drop('Functioning Day', axis=1)  # Filter and remove in one line

# Method 5: Boolean indexing + pop method
filtered_df = df[df['Functioning Day'] == 'Yes']  # Filter to new variable
filtered_df.pop('Functioning Day')  # Remove column with pop method
df = filtered_df  # Assign back to original variable name

# Method 6: Boolean indexing + columns selection
df = df[df['Functioning Day'] == 'Yes']  # Filter first
df = df[df.columns.drop('Functioning Day')]  # Keep all columns except specified one

# Method 7: Boolean indexing + inplace drop
df = df[df['Functioning Day'] == 'Yes'].copy()  # Create a filtered copy
df.drop('Functioning Day', axis=1, inplace=True)  # Remove column with inplace parameter
```

# Methods to Remove Columns in Pandas

|Method|Code|Explanation|
|---|---|---|
|drop Method|`data = data.drop("Functioning Day", axis=1)`|Standard method to remove columns. Returns new DataFrame.|
|drop Inplace|`data.drop("Functioning Day", axis=1, inplace=True)`|Same as above but modifies DataFrame in place without reassignment.|
|del Operator|`del data["Functioning Day"]`|Python's deletion operator. Removes column in place. Cannot be chained.|
|pop Method|`functioning_day = data.pop("Functioning Day")`|Removes column and returns it. Useful if you need the column data. In-place.|
|Column Subset|`data = data[[col for col in data.columns if col != "Functioning Day"]]`|Creates new DataFrame with subset of columns, excluding the unwanted one.|
|drop with list|`data = data.drop(columns=["Functioning Day"])`|Modern pandas syntax using 'columns' parameter instead of axis.|
|iloc with positions|`cols = [i for i, col in enumerate(data.columns) if col != "Functioning Day"]`<br>`data = data.iloc[:, cols]`|Selects columns by integer position excluding unwanted column.|
|rename + drop|`data = data.rename(columns={"Functioning Day": "_drop_me"}).drop("_drop_me", axis=1)`|Renames then drops. Useful in complex pipelines or to avoid string errors.|
# Methods to Convert Holiday Feature to Binary

|Method|Code|Explanation|
|---|---|---|
|map Method|`data['Holiday'] = data['Holiday'].map({'No Holiday': 0, 'Holiday': 1})`|Direct mapping of values|
|replace Method|`data['Holiday'] = data['Holiday'].replace({'No Holiday': 0, 'Holiday': 1})`|Uses replace function|
|Boolean Conversion|`data['Holiday'] = (data['Holiday'] == 'Holiday').astype(int)`|Boolean test converted to int|
|numpy where|`data['Holiday'] = np.where(data['Holiday'] == 'Holiday', 1, 0)`|Conditional assignment|

# Methods to Convert Seasons to One-Hot Encoding

## Method 1: Loop and Equality

```python
for season in ['Winter', 'Spring', 'Summer', 'Autumn']:
    data[season] = (data['Seasons'] == season).astype(int)
data.drop('Seasons', axis=1, inplace=True)
```

_Explanation:_ Creates separate columns manually

## Method 2: get_dummies

```python
season_dummies = pd.get_dummies(data['Seasons'])
data = pd.concaNOPW YUt([data, season_dummies], axis=1)
data.drop('Seasons', axis=1, inplace=True)
```

_Explanation:_ Creates all dummy columns at once

## Method 3: get_dummies with prefix

```python
data = pd.get_dummies(data, columns=['Seasons'], prefix='', prefix_sep='')
# No need to drop original column, it's dropped automatically
```

_Explanation:_ One-step approach with automatic column **removal**# Methods to Convert Date to Weekday Feature in Pandas
# Methods to Convert Date to Weekday Feature in Pandas

```python
# Method 1: dt.dayofweek + comparison
data['Weekday'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.dayofweek
data['Weekday'] = (data['Weekday'] >= 5).astype(int)
data = data.drop('Date', axis=1)

# Method 2: dt.day_name + isin
data['Weekday'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.day_name()
data['Weekday'] = data['Weekday'].isin(['Saturday', 'Sunday']).astype(int)
data = data.drop('Date', axis=1)

# Method 3: dt.weekday + comparison
data['Weekday'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.weekday > 4
data['Weekday'] = data['Weekday'].astype(int)
data = data.drop('Date', axis=1)

# Method 4: numpy where
data['Weekday'] = np.where(pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.dayofweek >= 5, 1, 0)
data = data.drop('Date', axis=1)

# Method 5: apply + lambda
data['Weekday'] = data['Date'].apply(lambda x: 1 if pd.to_datetime(x, format='%d/%m/%Y').weekday() >= 5 else 0)
data = data.drop('Date', axis=1)

# Method 6: map + custom function
def is_weekend(date_str):
    return int(pd.to_datetime(date_str, format='%d/%m/%Y').weekday() >= 5)
data['Weekday'] = data['Date'].map(is_weekend)
data = data.drop('Date', axis=1)
```

