import sys
import os
import pandas as pd

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 data_prep.py <filename (without .xlsx)>")
        sys.exit(1)

    base_name = sys.argv[1]
    xlsx_path = os.path.join('xlsx', f"{base_name}.xlsx")

    if not os.path.isfile(xlsx_path):
        print(f"Error: File '{xlsx_path}' not found.")
        sys.exit(1)

    # Read the Excel file
    df = pd.read_excel(xlsx_path)

    # Identify the first two columns as coordinate columns
    coord_columns = list(df.columns[:2])
    if len(coord_columns) < 2:
        print("Error: The file must have at least two columns for coordinates.")
        sys.exit(1)

    print(f"Identified coordinate columns: {coord_columns}")

    # Output folder: one level up from script (../CSV from xlsx, or ./CSV from root)
    output_dir = os.path.join('CSV')
    os.makedirs(output_dir, exist_ok=True)

    # Create one CSV per data column (include coordinates always)
    for column in df.columns[2:]:
        selected_data = df[coord_columns + [column]]
        safe_column_name = column.replace(' ', '_').replace('/', '_')
        output_path = os.path.join(output_dir, f"{safe_column_name}.csv")
        selected_data.to_csv(output_path, index=False, sep='\t')
        print(f"Saved {output_path}")

if __name__ == "__main__":
    main()
