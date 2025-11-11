import pandas as pd

# Read the CSV file (change filename if needed)
df = pd.read_csv('dellll.csv')

# Get list of all columns
all_columns = df.columns.tolist()
print("Columns in file:", all_columns)

# Preprocess each column
for col in all_columns:
    if col in ['ID', 'Abdominal Aortic Aneurysm', 'Operation Date']:  # Skip these columns
        continue
    
    if pd.api.types.is_numeric_dtype(df[col]):  # If numeric (integer/float), do nothing
        print(f"{col} is numeric → skipping")
        continue
    
    if df[col].dtype == 'object':  # If string (object)
        unique_vals = df[col].dropna().unique()  # Unique values excluding NaN
        
        if set(unique_vals) <= {'yes', 'no'}:  # Only yes/no values
            df[col] = df[col].map({'yes': 1, 'no': 0})
            print(f"{col} → converted: yes=1, no=0")
        else:
            # One-Hot Encoding for other string columns
            dummies = pd.get_dummies(df[col], prefix=col, dtype=int)
            df = pd.concat([df.drop(col, axis=1), dummies], axis=1)
            print(f"{col} → One-Hot encoded ({len(unique_vals)} unique values)")

# Save the processed file
df.to_csv('AAA_Processed4.csv', index=False)

print("\nDone! New file saved: AAA_Processed33.csv")
print("New shape:", df.shape)
print("New columns:", df.columns.tolist())
print("\nFirst 3 rows sample:")
print(df.head(3).to_string(index=False))