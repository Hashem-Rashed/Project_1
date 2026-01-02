from patient import Patient
from staff import Staff
class Department:
    """
    Represents a department within a hospital.

    Attributes:
        name (str): The name of the department.
        patients (list): A list of patients in the department.
        staff (list): A list of staff members assigned to the department.
    """

    def __init__(self, name):
        """
        Initialize a Department object.

        Args:
            name (str): Name of the department.
        """
        self.name = name
        self.patients = []  # Holds patient objects
        self.staff = []     # Holds staff objects

    def add_patient(self, patient : Patient):
        """
        Add a patient to the department.

        Args:
            patient: A Patient object with a 'name' attribute.
        """
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")
         
    def add_staff(self, staff_member : Staff):
        """
        Add a staff member to the department.

        Args:
            staff_member: A Staff object with a 'name' attribute.
        """
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")

    def __str__(self):
        """
        Return a user-friendly string representation of the department.

        Returns:
            str: Summary of department with counts of staff and patients.
        """
        return f"Department: {self.name} | Staff: {len(self.staff)} | Patients: {len(self.patients)}"

    def __repr__(self):
        """
        Return an official string representation for debugging.

        Returns:
            str: Detailed representation showing name, staff, and patients.
        """
        return f"Department(name={self.name!r}, staff={self.staff!r}, patients={self.patients!r})"
