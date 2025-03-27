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