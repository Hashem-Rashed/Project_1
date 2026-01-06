# Hospital_system/core/hospital.py
from .department import Department

class Hospital:
    """
    Class representing a hospital containing multiple departments.

    The Hospital class manages its departments and provides methods to
    add, remove, search, and list departments. It also calculates
    aggregated information about total patients and staff.

    Attributes:
        name (str): Name of the hospital.
        location (str): Physical location of the hospital.
        departments (list): List of Department objects belonging to the hospital.
    """

    def __init__(self, name, location):
        """
        Initialize a Hospital object with name and location.

        Args:
            name (str): Name of the hospital. Must be non-empty string.
            location (str): Physical location. Must be non-empty string.

        Raises:
            ValueError: If name or location is empty or not a string.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Hospital name must be a non-empty string.")
        if not isinstance(location, str) or not location.strip():
            raise ValueError("Hospital location must be a non-empty string.")

        self.name = name.strip()
        self.location = location.strip()
        self.departments = []

    def __str__(self):
        """Return a readable summary of the hospital."""
        return f"Hospital: {self.name} | Location: {self.location} | Departments: {len(self.departments)}"

    def __repr__(self):
        """Return detailed representation for debugging."""
        return f"Hospital(name={self.name!r}, location={self.location!r}, departments={self.departments!r})"

    def add_department(self, department):
        """
        Add a department if valid and not already present.

        Args:
            department (Department): Department object to add.

        Raises:
            TypeError: If department is not a Department instance.
            ValueError: If department name is empty or already exists.
        """
       

        if not isinstance(department, Department):
            raise TypeError("department must be a Department instance.")
        if not department.name or not department.name.strip():
            raise ValueError("Department must have a non-empty name.")
        if any(d.name == department.name for d in self.departments):
            raise ValueError(f"Department '{department.name}' already exists in {self.name}.")

        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    def remove_department(self, department_name):
        """
        Remove a department by its name.

        Args:
            department_name (str): Name of the department to remove.

        Returns:
            bool: True if removed, False if not found.

        Raises:
            ValueError: If department_name is empty.
        """
        if not department_name or not isinstance(department_name, str):
            raise ValueError("Department name must be a non-empty string.")

        for dept in self.departments:
            if dept.name == department_name:
                self.departments.remove(dept)
                print(f"Department '{department_name}' removed from {self.name}.")
                return True
        print(f"Department '{department_name}' not found in {self.name}.")
        return False

    def find_department(self, department_name):
        """
        Find and return a department by name.

        Args:
            department_name (str): Name of the department to find.

        Returns:
            Department | None: The Department object if found, else None.

        Raises:
            ValueError: If department_name is empty.
        """
        if not department_name or not isinstance(department_name, str):
            raise ValueError("Department name must be a non-empty string.")
        for dept in self.departments:
            if dept.name == department_name:
                return dept
        return None

    def list_departments(self):
        """
        Print an enumerated list of department names.

        Returns:
            int: Number of departments.
        """
        print(f"\nDepartments in {self.name}:")
        if not self.departments:
            print("  No departments available.")
        else:
            for idx, dept in enumerate(self.departments, 1):
                print(f"  {idx}. {dept.name}")
        return len(self.departments)

    def get_total_patients(self):
        """Return total number of patients across all departments."""
        return sum(dept.get_patient_count() for dept in self.departments)

    def get_total_staff(self):
        """Return total number of staff across all departments."""
        return sum(dept.get_staff_count() for dept in self.departments)

    def view_hospital_info(self):
        """Print full hospital information including departments, patients, and staff."""
        print("\n" + "=" * 50)
        print(f"HOSPITAL: {self.name}")
        print(f"Location: {self.location}")
        print(f"Total Departments: {len(self.departments)}")
        print(f"Total Patients: {self.get_total_patients()}")
        print(f"Total Staff: {self.get_total_staff()}")
        for dept in self.departments:
            print(f"\nDepartment: {dept.name} | Staff: {len(dept.staff)} | Patients: {len(dept.patients)}")
        print("=" * 50)
