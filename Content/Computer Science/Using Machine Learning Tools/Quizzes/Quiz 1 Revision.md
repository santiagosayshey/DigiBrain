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

## Methods For Converting "Holiday" to Binary (0/1)

```python
# Method 1: Using map() function
df['Holiday'] = df['Holiday'].map({'No': 0, 'Yes': 1})  # Maps 'No' to 0 and 'Yes' to 1

# Method 2: Using replace() function
df['Holiday'] = df['Holiday'].replace({'No': 0, 'Yes': 1})  # Replaces values according to dictionary

# Method 3: Using get_dummies() and selecting one column
df['Holiday'] = pd.get_dummies(df['Holiday'], drop_first=True)  # Creates dummy variables and keeps only one column (1 for 'Yes')

# Method 4: Using astype() after equality comparison
df['Holiday'] = (df['Holiday'] == 'Yes').astype(int)  # Compares to 'Yes', returns True/False, converts to 1/0

# Method 5: Using numpy where
import numpy as np
df['Holiday'] = np.where(df['Holiday'] == 'Yes', 1, 0)  # Returns 1 where 'Yes', 0 otherwise

# Method 6: Using lambda function
df['Holiday'] = df['Holiday'].apply(lambda x: 1 if x == 'Yes' else 0)  # Applies the lambda to each element
```

## Methods For Converting "Season" to One-Hot Encoding

```python
# Method 1: Using get_dummies() and concat
season_dummies = pd.get_dummies(df['Season'], prefix='')  # Create dummies with empty prefix
season_dummies.columns = ['Winter', 'Spring', 'Summer', 'Autumn']  # Rename columns
df = pd.concat([df, season_dummies], axis=1)  # Add to DataFrame
df = df.drop('Season', axis=1)  # Remove original column

# Method 2: Using get_dummies() directly with column renaming
season_dummies = pd.get_dummies(df['Season'])  # Create dummies
season_dummies.columns = ['Winter', 'Spring', 'Summer', 'Autumn']  # Rename columns 
df = pd.concat([df, season_dummies], axis=1)  # Add to DataFrame
df = df.drop('Season', axis=1)  # Remove original column

# Method 3: Manual creation with dictionary mapping
season_mapping = {'Winter': 'Winter', 'Spring': 'Spring', 'Summer': 'Summer', 'Autumn': 'Autumn'}
for season in season_mapping.keys():
    df[season] = (df['Season'] == season).astype(int)  # Create column for each season
df = df.drop('Season', axis=1)  # Remove original column

# Method 4: Using pandas crosstab
seasons = pd.crosstab(df.index, df['Season'])  # Create crosstab with index and Season
seasons.columns = ['Winter', 'Spring', 'Summer', 'Autumn']  # Rename columns
df = pd.concat([df, seasons], axis=1)  # Add to DataFrame
df = df.drop('Season', axis=1)  # Remove original column

# Method 5: Using sklearn OneHotEncoder
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse=False)
season_encoded = encoder.fit_transform(df[['Season']])  # Encode Season
season_df = pd.DataFrame(season_encoded, columns=['Winter', 'Spring', 'Summer', 'Autumn'])  # Convert to DataFrame
df = pd.concat([df, season_df], axis=1)  # Add to DataFrame
df = df.drop('Season', axis=1)  # Remove original column

# Method 6: Using for loop with iterative assignment
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
for season in seasons:
    df[season] = 0  # Initialize with zeros
    df.loc[df['Season'] == season, season] = 1  # Set to 1 where Season matches
df = df.drop('Season', axis=1)  # Remove original column
```
## Methods For Converting Date to Weekday Binary Feature

```python
# Method 1: Using pandas dt.dayofweek accessor
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime if not already
df['Weekday'] = (df['Date'].dt.dayofweek < 5).astype(int)  # 0-4 are weekdays (Mon-Fri), 5-6 are weekend
df = df.drop('Date', axis=1)  # Remove the original Date column

# Method 2: Using pandas dt.weekday accessor with comparison
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime if not already
df['Weekday'] = (~df['Date'].dt.weekday.isin([5, 6])).astype(int)  # Not in [5,6] means weekday
df = df.drop('Date', axis=1)  # Remove the original Date column

# Method 3: Using numpy where with weekday check
import numpy as np
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime if not already
df['Weekday'] = np.where(df['Date'].dt.weekday < 5, 1, 0)  # 1 for weekday, 0 for weekend
df = df.drop('Date', axis=1)  # Remove the original Date column

# Method 4: Using apply with a lambda function
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime if not already
df['Weekday'] = df['Date'].apply(lambda x: 1 if x.weekday() < 5 else 0)  # 1 for weekday, 0 for weekend
df = df.drop('Date', axis=1)  # Remove the original Date column

# Method 5: Using pandas dt.dayofweek with map
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime if not already
df['Weekday'] = df['Date'].dt.dayofweek.map(lambda x: 1 if x < 5 else 0)  # Map 0-4 to 1, 5-6 to 0
df = df.drop('Date', axis=1)  # Remove the original Date column

# Method 6: Using pandas dt.day_name with conditional logic
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime if not already
weekend_days = ['Saturday', 'Sunday']
df['Weekday'] = (~df['Date'].dt.day_name().isin(weekend_days)).astype(int)  # Not in weekend days is weekday
df = df.drop('Date', axis=1)  # Remove the original Date column
```