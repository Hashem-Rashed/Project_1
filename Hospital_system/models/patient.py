from models import Person

class Patient(Person):
    """
    Class representing a hospital patient.

    Inherits from Person and stores medical record information.
    Patients can view their records, check in/out of the hospital, 
    and have a status to indicate if they are currently active in the hospital.

    Attributes:
        name (str): Full name of the patient.
        date_of_birth (date): Date of birth.
        medical_record (str): The patient's medical record. Cannot be empty.
        status (str): Current status of the patient, either 'in' or 'out'.
    """

    def __init__(self, name, date_of_birth, medical_record):
        """
        Initialize a Patient object.

        Args:
            name (str): Full name of the patient.
            date_of_birth (date): Patient's date of birth.
            medical_record (str): Patient's medical record.

        Raises:
            ValueError: If medical_record is empty.
        """
        super().__init__(name, date_of_birth)
        if not medical_record or not medical_record.strip():
            raise ValueError("Medical record cannot be empty")
        self.medical_record = medical_record
        self.status = "out"  # Default status is checked out

    def __str__(self):
        """Return a readable string including name, age, medical record, and status."""
        return f"{super().__str__()}, Medical Record: {self.medical_record}, Status: {self.status}"

    def __repr__(self):
        """Return a developer-friendly string for debugging."""
        return (
            f"Patient(name={self.name!r}, "
            f"date_of_birth={self.date_of_birth!r}, "
            f"medical_record={self.medical_record!r}, "
            f"status={self.status!r})"
        )

    def view_record(self):
        """
        View the patient's medical record.

        Returns:
            str: Formatted medical record string.
        """
        return f"Medical Record for {self.name}: {self.medical_record}"

    def check_in(self):
        """
        Mark the patient as checked in.

        Returns:
            str: Confirmation message.
        """
        if self.status == "in":
            return f"{self.name} is already checked in."
        self.status = "in"
        return f"{self.name} has checked in."

    def check_out(self):
        """
        Mark the patient as checked out.

        Returns:
            str: Confirmation message.
        """
        if self.status == "out":
            return f"{self.name} is already checked out."
        self.status = "out"
        return f"{self.name} has checked out."

    def is_active(self):
        """
        Check if the patient is currently active (checked in).

        Returns:
            bool: True if checked in, False otherwise.
        """
        return self.status == "in"
