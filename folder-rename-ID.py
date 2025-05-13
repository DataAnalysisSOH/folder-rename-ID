import os
import pandas as pd

# Path to your Excel file
csv_file = r"C:/Users/yuqia/Documents/GitHub/parx/folder-rename-ID/EEID and name and Associate ID.csv"

# Directory containing the folders to rename
base_folder = r"C:/Users/yuqia/Downloads/Employees/Employees"

# Read the CSV file
df = pd.read_csv(csv_file)

# Iterate through each row in the DataFrame
for _, row in df.iterrows():
    soh_id = str(row['EEID']).strip()
    associated_id = str(row['ADP_Associated_ID']).strip()
    first_name = str(row['First Name']).strip()
    last_name = str(row['Last Name']).strip()
     # Construct the old folder name
    old_folder_name = f"{soh_id}-{first_name}.{last_name}"
    # Construct the new folder name
    new_folder_name = f"{associated_id}-{old_folder_name}"
    
    # Construct the full path for the new folder
    new_folder_path = os.path.join(base_folder, new_folder_name)

    # Create the new folder
    try:
        os.makedirs(new_folder_path, exist_ok=True)
        print(f"Created: {new_folder_path}")
    except Exception as e:
        print(f"Failed to create {new_folder_path}: {e}")
