class Hospital:
    """
    Class representing a hospital, containing multiple departments.

    This class manages departments within the hospital and provides
    methods to add, remove, and find departments. It also provides
    aggregated information about the hospital such as total patients
    and staff across all departments.

    Attributes:
        name (str): Name of the hospital.
        location (str): Physical location of the hospital.
        departments (list): List of Department objects within the hospital.
    """

    def __init__(self, name, location):
        """
        Initialize a Hospital object.

        Args:
            name (str): Name of the hospital.
            location (str): Physical location of the hospital.
        """
        self.name = name
        self.location = location
        self.departments = []

    def __str__(self):
        """
        Return a user-friendly string representation of the hospital.

        Returns:
            str: A readable string showing the hospital's name, location,
                 and number of departments.
        """
        return f"Hospital: {self.name} | Location: {self.location} | Departments: {len(self.departments)}"

    def __repr__(self):
        """
        Return a detailed string representation of the hospital for debugging.

        Returns:
            str: A precise representation showing all attributes.
        """
        return f"Hospital(name={self.name!r}, location={self.location!r}, departments={self.departments!r})"

    def add_department(self, department):
        """
        Add a department to the hospital if it does not already exist.

        Args:
            department: Department object to add.
        """
        if department not in self.departments:
            self.departments.append(department)
            print(f"Department '{department.name}' added to {self.name}")
        else:
            print(f"Department '{department.name}' already exists in {self.name}")

    def remove_department(self, department_name):
        """
        Remove a department from the hospital by name.

        Args:
            department_name (str): Name of the department to remove.

        Returns:
            bool: True if department was removed, False if not found.
        """
        for dept in self.departments:
            if dept.name == department_name:
                self.departments.remove(dept)
                print(f"Department '{department_name}' removed from {self.name}")
                return True
        print(f"Department '{department_name}' not found")
        return False

    def find_department(self, department_name):
        """
        Find a department by name.

        Args:
            department_name (str): Name of the department to find.

        Returns:
            Department or None: The Department object if found, otherwise None.
        """
        for dept in self.departments:
            if dept.name == department_name:
                return dept
        return None

    def list_departments(self):
        """
        List all departments in the hospital.

        Prints the departments in an enumerated list.

        Returns:
            int: Number of departments in the hospital.
        """
        print(f"\nDepartments in {self.name}:")
        if not self.departments:
            print("  No departments")
        else:
            for i, dept in enumerate(self.departments, 1):
                print(f"  {i}. {dept}")
        return len(self.departments)

    def get_total_patients(self):
        """
        Calculate the total number of patients across all departments.

        Returns:
            int: Total number of patients.
        """
        total = 0
        for dept in self.departments:
            total += dept.get_patient_count()
        return total

    def get_total_staff(self):
        """
        Calculate the total number of staff across all departments.

        Returns:
            int: Total number of staff.
        """
        total = 0
        for dept in self.departments:
            total += dept.get_staff_count()
        return total

    def view_hospital_info(self):
        """
        Display detailed information about the hospital.

        Prints the hospital's name, location, total departments,
        total patients, and total staff.
        """
        print("\n" + "=" * 50)
        print(f"HOSPITAL: {self.name}")
        print(f"Location: {self.location}")
        print(f"Total Departments: {len(self.departments)}")
        print(f"Total Patients: {self.get_total_patients()}")
        print(f"Total Staff: {self.get_total_staff()}")
        print("=" * 50)
