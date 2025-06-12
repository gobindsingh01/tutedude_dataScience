import sys

emp_details = {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}

def menu():
    print()
    print("1. Add Employee")
    print("2. View All Employee")
    print("3. Search for Employee")
    print("4. Exit")

def add_employee():
    print("Enter Employee details : ")
    emp_id = int(input("Enter Employee id number : "))
    if emp_id not in emp_details :
        name= input("Enter Employee Name : ")
        age = int(input("Enter Employee Age : "))
        department = input("Enter Employee Department : ")
        salary = int(input("Enter Employee Salary : "))
        emp_details[emp_id] = {
            "name" : name,
            "age" : age,
            "department" : department,
            "salary" : salary
        }
        print("\nEmployee", emp_id, "has been successfully added!\n")
    else : 
        print("\nEmployee id is already in use. Enter an unique one.\n")

def view_employees():
    if len(emp_details)>0:
        print()
        print(len(emp_details),"employee found! \n")
        print("\nShowing all the employees :\n")
        for emp in emp_details:
            print("Employee id :",emp)
            print("Name :",emp_details[emp]['name'])
            print("Age :",emp_details[emp]["age"])
            print("Department :",emp_details[emp]["department"])
            print("Salary :",emp_details[emp]["salary"])
            print()
    else:
        print("\nNo employees available.\n")

def search_employee():
    emp_id = int(input("Enter employee id for search : "))
    if emp_id in emp_details:
            print("Employee id :",emp_id)
            print("Name :",emp_details[emp_id]['name'])
            print("Age :",emp_details[emp_id]["age"])
            print("Department :",emp_details[emp_id]["department"])
            print("Salary :",emp_details[emp_id]["salary"])
            print()
    else:
        print("\nEmployee not found.\n")


while True:
    menu()
    choice = input("\nchoose the option and enter the number : ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        print("\nThank You!")
        sys.exit()
    else:
        print("\nEnter a valid number from 1-4\n")