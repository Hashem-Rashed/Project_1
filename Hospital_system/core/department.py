# Hospital_system/core/department.py
from Hospital_system.models.patient import Patient
from Hospital_system.models.staff import Staff


class Department:
    """
    Class representing a department within a hospital.

    A department manages its own patients and staff. It provides methods
    to add patients and staff, and offers string representations for
    both user-friendly display and debugging.

    Attributes:
        name (str): The name of the department.
        patients (list): List of Patient objects assigned to this department.
        staff (list): List of Staff objects assigned to this department.
    """

    def __init__(self, name):
        """
        Initialize a Department object.

        Args:
            name (str): Name of the department.
        """
        self.name = name
        self.patients = []
        self.staff = []

    def __str__(self):
        """
        Return a user-friendly string representation of the department.

        Returns:
            str: A readable summary of the department, including counts
                 of staff and patients.
        """
        return f"Department: {self.name} | Staff: {len(self.staff)} | Patients: {len(self.patients)}"

    def __repr__(self):
        """
        Return a detailed string representation of the department for debugging.

        Returns:
            str: Official representation showing the name, staff list, and patients list.
        """
        return f"Department(name={self.name!r}, staff={self.staff!r}, patients={self.patients!r})"

    def add_patient(self, patient):
        """
        Add a patient to the department.

        Args:
            patient (Patient): Patient object to add to this department.

        Prints:
            Confirmation message after adding the patient.
        """
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        """
        Add a staff member to the department.

        Args:
            staff_member (Staff): Staff object to add to this department.

        Prints:
            Confirmation message after adding the staff member.
        """
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def get_patient_count(self):
        """
        Get the number of patients in the department.

        Returns:
            int: Number of patients.
        """
        return len(self.patients)

    def get_staff_count(self):
        """
        Get the number of staff members in the department.

        Returns:
            int: Number of staff members.
        """
        return len(self.staff)
