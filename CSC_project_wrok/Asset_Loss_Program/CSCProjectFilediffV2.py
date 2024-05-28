import csv
from datetime import datetime

def create_file_function():
    header = ["S.No.","Expense","Amount","Type","Date","Time","Remarks"]
    with open('data_file.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        file.close()

def backed_check_function():
    print("Running a Backed Check")
    try:
        with open('data_file.csv', mode='r',newline='') as file:
            pass
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        create_file_function()

def get_file_function():
    data = []
    with open('data_file.csv', mode='r',newline='') as file:
        reader = csv.reader(file)
        for i in reader:
            data.append(i)
    return data

def enter_entry_function():
    temp_data = get_file_function()
    length = len(temp_data)
    if length > 1:
        sno = length
    else:
        sno = 1
    expense = input('Enter the category of the Expense\nEnter here:')
    amount = int(input('Enter the amount for the expese\nEnter here:'))
    type = 0
    while True:
        n = input('Enter the type of expense\n1)Asset(1)\n2)Liability(2)\nEnter here:')
        if n == "1":
            type = "Asset"
            break
        elif n == "2":
            type = "Liability"
            break
        else:
            print("Invalid input please try again")
            continue
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    remarks = input("Please enter remarks for your entry\nEnter here:")
    new_data_entry = [sno, expense, amount, type , date, time , remarks]
    with open('data_file.csv', 'a' , newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_data_entry)
        file.close()
    print("Entry added successfully")

def update_entry_function():
    temp_data = get_file_function()
    get_sno = int(input("Enter the the Serial Number of the Expense\nEnter here:"))
    get_expense = input('Enter the new category of the Expense\nEnter here:')
    get_amount = int(input('Enter the new amount for the expese\nEnter here:'))
    get_type = 0
    while True:
        n = input('Enter the new type of expense\n1)Asset(1)\n2)Liability(2)\nEnter here:')
        if n == "1":
            get_type = "Asset"
            break
        elif n == "2":
            get_type = "Liability"
            break
        else:
            print("Invalid input please try again")
            continue
    get_date = temp_data[get_sno][4]
    get_time = temp_data[get_sno][5]
    get_remarks = input('Enter the new remarks for the entry\nEnter here:')
    temp_data[get_sno] = [get_sno, get_expense, get_amount, get_type ,get_date, get_time , get_remarks]
    with open('data_file.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(temp_data)
        file.close()
    print("Entery updated successfully")

def track_expenditure_function():
    while True:
        tef_ans = int(input("What would you like to?\n1)Get monthly expenditure(1)\n2)Get yearly expenditure(2)\n3)Get total expediture(3)\n4)Get expenditure on a perticular category(4)\nEnter here:"))
        if tef_ans == 1:
            temp_data = get_file_function()
            temp_data.pop(0)
            temp_ans = input("Enter the Month(in numarical MM) that you would like to veiw the expenditue for\nEnter here:")
            temp_month_data = []
            temp_month_data_total = 0
            for i in temp_data:
                month = i[4].split('/')
                if month[1] == temp_ans:
                    temp_month_data.append(i)
                    if i[3] == "Asset":
                        temp_month_data_total += int(i[2])
                    elif i[3] == "Liability":
                        temp_month_data_total -= int(i[2])
                    else:
                        print("Invalid entries in file please recheak the file or create a new one")
                        exit()
            for i in temp_month_data:
                print(i)
            print("Monthly Total:" , temp_month_data_total)
        elif tef_ans == 2:
            temp_data = get_file_function()
            temp_data.pop(0)
            temp_ans = input("Enter the Year(in numarical YYYY) that you would like to veiw the expenditue for\nEnter here:")
            temp_year_data = []
            temp_year_data_total = []
            for i in temp_data:
                year = i[5].split('/')
                if year[2] == temp_ans:
                    temp_year_data.append(i)
                    if i[3] == "Asset":
                        temp_year_data_total += int(i[2])
                    elif i[3] == "Liability":
                        temp_year_data_total -= int(i[2])
                    else:
                        print("Invalid entries in file please recheak the file or create a new file")
                        exit()
            for i in temp_year_data:
                print(i)
            print("Yearly Total:" , temp_year_data_total)
        elif tef_ans == 3:
            temp_data = get_file_function()
            temp_data.pop(0)
            temp_total_expenditure_data_total = 0
            for i in temp_data:
                if i[3] == "Asset":
                    temp_total_expenditure_data_total += int(i[2])
                elif i[3] == "Liability":
                    print(type(i[2]))
                    temp_total_expenditure_data_total -= int(i[2])
                else:
                    print("Invalid entries in file please recheak the file or create a new file")
            for i in temp_data:
                print(i)
            print("Total:" , temp_total_expenditure_data_total)
        elif tef_ans == 4:
            temp_data = get_file_function()
            temp_data.pop(0)
            t = input("Enter the category of the expense you would like to view: ")
            temp_category_data = []
            temp_category_data_total = 0
            for i in temp_data:
                if i[1]==t:
                    temp_category_data.append(i)
                    if i[3] == "Asset":
                        temp_category_data_total += int(i[2])
                    elif i[3] == "Liability":
                        temp_category_data_total -= int(i[2])
                    else:
                        print("Invalid entries in file please recheak the file or create a new file")
            for i in temp_category_data:
                print(i)
            print("Category Total:" , temp_category_data_total)
        else:
            print('invalid input please try again')
            continue


def save_to_file():
    temp_data = get_file_function()
    with open("Finanacial Data.csv", "w",newline='') as file:
        writer = csv.writer(file)
        writer.writerows(temp_data)
        file.close()
        print("File saved successfully")


def menu():
    print('Welcome to Finanacial data tracker')
    while True:
        backed_check_function()
        print('What would you like to do?')
        menu_answer= int(input('1)Add a new entry\n2)Udate an entry\n3)Track your expenditure\n4)Save data to your file\n5)exit\nEnter here:'))
        if menu_answer == 1:
            enter_entry_function()
        elif menu_answer == 2:
            update_entry_function()
        elif menu_answer == 3:
            track_expenditure_function()
        elif menu_answer == 4:
            save_to_file()
        elif menu_answer == 5:
            exit()
        else:
            print('Invalid input please try again')
            continue

menu()