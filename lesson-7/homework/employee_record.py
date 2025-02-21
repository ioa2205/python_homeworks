import os
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.employee_name = name
        self.employee_position = position
        self.employee_salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.employee_name}, {self.employee_position}, {self.employee_salary}"

import os

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        # Ensure file exists to avoid errors
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as f:
                pass  # Create an empty file if it doesn't exist

    def add_employee(self, employee):
        """Adds a new employee record to the file."""
        with open(self.FILE_NAME, "a") as f:
            f.write(f"{employee.employee_id},{employee.employee_name},{employee.employee_position},{employee.employee_salary}\n")
        print("✅ Employee added successfully!")

    def view_employees(self):
        """Displays all employee records."""
        if not os.path.exists(self.FILE_NAME) or os.stat(self.FILE_NAME).st_size == 0:
            print("⚠ No employees found!")
            return

        print("\n📜 Employee Records:")
        with open(self.FILE_NAME, "r") as f:
            for line in f:
                print(line.strip())

    def search_employee(self, employee_id):
        """Search for an employee by ID."""
        with open(self.FILE_NAME, "r") as f:
            for line in f:
                emp_data = line.strip().split(",")
                if emp_data[0] == employee_id:
                    print(f"\n🔍 Employee Found: {line.strip()}")
                    return
        print("❌ Employee not found!")

    def update_employee(self, employee_id, new_name=None, new_position=None, new_salary=None):
        """Updates an employee's information based on Employee ID."""
        employees = []
        found = False

        with open(self.FILE_NAME, "r") as f:
            for line in f:
                emp_data = line.strip().split(",")
                if emp_data[0] == employee_id:
                    found = True
                    emp_data[1] = new_name if new_name else emp_data[1]
                    emp_data[2] = new_position if new_position else emp_data[2]
                    emp_data[3] = str(new_salary) if new_salary else emp_data[3]
                employees.append(",".join(emp_data))

        if found:
            with open(self.FILE_NAME, "w") as f:
                f.write("\n".join(employees) + "\n")
            print("✅ Employee updated successfully!")
        else:
            print("❌ Employee not found!")

    def delete_employee(self, employee_id):
        """Deletes an employee from the file."""
        employees = []
        found = False

        with open(self.FILE_NAME, "r") as f:
            for line in f:
                emp_data = line.strip().split(",")
                if emp_data[0] == employee_id:
                    found = True
                    continue  # Skip this employee
                employees.append(line.strip())

        if found:
            with open(self.FILE_NAME, "w") as f:
                f.write("\n".join(employees) + "\n")
            print("✅ Employee deleted successfully!")
        else:
            print("❌ Employee not found!")

    def menu(self):
        """Displays a menu for user interaction."""
        while True:
            print("\n📂 Employee Records Manager")
            print("1️⃣ Add new employee record")
            print("2️⃣ View all employee records")
            print("3️⃣ Search for an employee by Employee ID")
            print("4️⃣ Update an employee's information")
            print("5️⃣ Delete an employee record")
            print("6️⃣ Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(emp_id, name, position, salary)
                self.add_employee(employee)

            elif choice == "2":
                self.view_employees()

            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ")
                self.search_employee(emp_id)

            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter New Name (press Enter to skip): ") or None
                position = input("Enter New Position (press Enter to skip): ") or None
                salary = input("Enter New Salary (press Enter to skip): ") or None
                self.update_employee(emp_id, name, position, salary)

            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_employee(emp_id)

            elif choice == "6":
                print("👋 Goodbye!")
                break

            else:
                print("⚠ Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()