import csv

def create_csv_file(filename):
    header = ["Category", "Type", "Amount"]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def add_entry_to_csv(filename, entry):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(entry)

def view_csv_data(filename, category=None):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if category is None or row[0] == category:
                print(row)

def calculate_total(filename, category=None):
    total = 0
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if category is None or row[0] == category:
                total += float(row[2])
    return total

def check_file_existence(filename):
    try:
        with open(filename, mode='r'):
            # Check if the file exists
            pass

    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new file.")
        create_csv_file(filename)

def menu():
    filename = "financial_data.csv"
    check_file_existence(filename)

    while True:
        print("\nMenu:")
        print("1. Add Entry")
        print("2. View Data")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            category_input = input("Enter the category (1 for Asset, 2 for Liability): ")
            category = "Asset" if category_input == "1" else "Liability"
            entry_type = input("Enter the type: ")
            amount = input("Enter the amount: ")
            add_entry_to_csv(filename, [category, entry_type, amount])
            print("Entry added successfully.")

        elif choice == "2":
            category_input = input("Enter category (1 for Asset, 2 for Liability): ")
            category = "Asset" if category_input == "1" else "Liability"
            view_csv_data(filename, category)

        elif choice == "3":
            category_input = input("Enter category (1 for Asset, 2 for Liability): ")
            category = "Asset" if category_input == "1" else "Liability"
            total = calculate_total(filename, category)
            print("Total amount: {}".format(total))

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    menu()
