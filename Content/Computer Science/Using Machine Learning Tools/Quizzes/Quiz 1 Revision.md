# Methods to Filter Rows by Condition in Pandas

| Method                         | Code                                                                                                                                                              | Explanation                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Boolean Indexing               | `data = data[data["Functioning Day"] == "Yes"]`                                                                                                                   | Creates a boolean mask and uses it to filter the DataFrame. Most common approach. |
| query Method                   | `data = data.query("`Functioning Day `== 'Yes'")`                                                                                                                 | Uses SQL-like syntax for filtering. Readable for simple conditions.               |
| loc Indexer                    | `data = data.loc[data["Functioning Day"] == "Yes"]`                                                                                                               | Location-based indexer with boolean condition.                                    |
| drop with indices              | `data = data.drop(data[data["Functioning Day"] == "No"].index)`                                                                                                   | Identifies indices where condition is false and drops those rows.                 |
| Boolean Indexing (inplace alt) | `data = data[data["Functioning Day"] == "Yes"].copy()`                                                                                                            | Similar to first method but creates a new copy explicitly.                        |
| mask + dropna                  | `data["_temp"] = data["Functioning Day"].mask(data["Functioning Day"] != "Yes")`<br>`data = data.dropna(subset=["_temp"])`<br>`data = data.drop("_temp", axis=1)` | Creates temporary masked column and drops rows with NaN.                          |
| filter Method                  | `data = data.filter(items=data.index[data["Functioning Day"] == "Yes"], axis=0)`                                                                                  | Uses filter method with pre-computed index locations.                             |
| df.where                       | `data = data.where(data["Functioning Day"] == "Yes").dropna()`                                                                                                    | Replaces non-matching rows with NaN, then drops NaN rows.                         |

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

| Method                  | Code                                                                                                                                                                   | Explanation                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Loop and Equality       | `for season in ['Winter', 'Spring', 'Summer', 'Autumn']:`<br> `data[season] = (data['Seasons'] == season).astype(int)`<br>`data.drop('Seasons', axis=1, inplace=True)` | Creates separate columns manually               |
| get_dummies             | `season_dummies = pd.get_dummies(data['Seasons'])`<br>`data = pd.concat([data, season_dummies], axis=1)`<br>`data.drop('Seasons', axis=1, inplace=True)`               | Creates all dummy columns at once               |
| get_dummies with prefix | `data = pd.get_dummies(data, columns=['Seasons'], prefix='', prefix_sep='')`<br>`# No need to drop original column, it's dropped automatically`                        | One-step approach with automatic column removal |
# Methods to Convert Date to Weekday Feature in Pandas

# Methods to Convert Date to Weekday Feature in Pandas

|Method|Code|Explanation|
|---|---|---|
|dt.dayofweek + comparison|```python||
|data['Weekday'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.dayofweek|||
|data['Weekday'] = (data['Weekday'] >= 5).astype(int)|||

````|
| dt.day_name + isin | ```python
data['Weekday'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.day_name()
data['Weekday'] = data['Weekday'].isin(['Saturday', 'Sunday']).astype(int)
``` | Convert to day names and check if in weekend list |
| dt.weekday + comparison | ```python
data['Weekday'] = pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.weekday > 4
data['Weekday'] = data['Weekday'].astype(int)
``` | Simplified version using boolean comparison with automatic type conversion |
| numpy where | ```python
data['Weekday'] = np.where(pd.to_datetime(data['Date'], format='%d/%m/%Y').dt.dayofweek >= 5, 1, 0)
``` | Single-line approach using numpy's conditional function |
| apply + lambda | ```python
data['Weekday'] = data['Date'].apply(lambda x: 1 if pd.to_datetime(x, format='%d/%m/%Y').weekday() >= 5 else 0)
``` | Using apply with lambda function for row-wise processing |
| map + custom function | ```python
def is_weekend(date_str):
    return int(pd.to_datetime(date_str, format='%d/%m/%Y').weekday() >= 5)
data['Weekday'] = data['Date'].map(is_weekend)
``` | Using a named function with map for clarity and reusability |
````