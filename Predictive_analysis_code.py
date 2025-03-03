import pandas as pd
from rapidfuzz import fuzz, process

# Load the mock database (replace with the correct path to your file)
file_path = r"C:\Users\harsh\OneDrive - UBC\4th year FILES\ENGR 499 - CAPSTONE\Mock_Central_Equipment_List.xlsx"
df = pd.read_excel(file_path)


# Function for fuzzy matching on Tag_No
def fuzzy_search(column, search_term, threshold=70):
    """
    Perform a fuzzy search on the specified column of the database.
    Returns rows where the match score is above the threshold.
    """
    matches = process.extract(search_term, df[column].astype(str), scorer=fuzz.partial_ratio, limit=10)
    filtered_matches = [match for match in matches if match[1] >= threshold]
    return filtered_matches

# Function to get rows based on matched results
def get_matched_rows(column, matches):
    """
    Retrieve rows from the DataFrame based on fuzzy matches.
    """
    matched_values = [match[0] for match in matches]
    return df[df[column].astype(str).isin(matched_values)]

# Function to display results in a user-friendly format
def display_results(results):
    """
    Display the matching rows in a user-friendly format.
    """
    if results.empty:
        print("No matches found.")
    else:
        print(results.to_string(index=False))

# Main program loop
while True:
    print("\n--- Predictive Analysis Tool ---")
    print("Options:")
    print("1. Search by Tag_No")
    print("2. Search by Instrument Type")
    print("3. Search by PID Number")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("Exiting the program. Goodbye!")
        break

    if choice == "1":
        search_column = "Tag_No"
    elif choice == "2":
        search_column = "Instrument_Type"
    elif choice == "3":
        search_column = "PID_No"
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue

    search_term = input(f"Enter your search term for {search_column}: ")
    matches = fuzzy_search(search_column, search_term)
    results = get_matched_rows(search_column, matches)
    display_results(results)


