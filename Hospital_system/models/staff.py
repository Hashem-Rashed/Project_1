from datetime import date
from models import Person
from models import Patient  # Ensure correct typing


class Staff(Person):
    """
    Class representing a hospital staff member, inheriting from Person.

    Extends the base Person class to include attributes and methods
    specific to hospital staff, such as position, schedule, and patient care actions.

    Attributes:
        name (str): Full legal name of the staff member.
        date_of_birth (date): Staff member's date of birth.
        position (str): Job title or role within the hospital.
        schedule (str | None): Work schedule for the staff member, defaults to None.
    """

    def __init__(self, name: str, date_of_birth: date, position: str) -> None:
        """
        Initialize a Staff object.

        Args:
            name (str): Full legal name of the staff member.
            date_of_birth (date): Date of birth of the staff member.
            position (str): Job title or role.

        Raises:
            ValueError: If position is empty.
        """
        super().__init__(name, date_of_birth)
        if not position or not position.strip():
            raise ValueError("Position cannot be empty")
        self.position = position
        self.schedule = None

    def __str__(self) -> str:
        """Return a user-friendly string representation of the staff member."""
        return f"Staff Name: {self.name}, Age: {self.get_age()}, Position: {self.position}"

    def __repr__(self) -> str:
        """Return a detailed string representation of the staff member for debugging."""
        return (
            f"Staff(name={self.name!r}, date_of_birth={self.date_of_birth!r}, "
            f"position={self.position!r}, schedule={self.schedule!r})"
        )

    def view_info(self) -> str:
        """
        Display key information about the staff member.

        Returns:
            str: Formatted string with name, age, and position.
        """
        return str(self)

    def set_schedule(self, schedule: str) -> None:
        """
        Assign a work schedule to the staff member.

        Args:
            schedule (str): Schedule description.
        """
        self.schedule = schedule

    def view_schedule(self) -> str:
        """
        View the staff member's current schedule.

        Returns:
            str: Formatted string showing the schedule.
        """
        return f"{self.name}'s Schedule: {self.schedule or 'Not set'}"

    def diagnose_patient(self, patient: Patient, diagnosis: str) -> str:
        """
        Record a diagnosis for a patient.

        Args:
            patient (Patient): The patient being diagnosed.
            diagnosis (str): The diagnosis details.

        Returns:
            str: Confirmation message.
        """
        return f"{self.name} diagnosed {patient.name} with: {diagnosis}"

    def prescribe_treatment(self, patient: Patient, treatment: str) -> str:
        """
        Prescribe treatment for a patient.

        Args:
            patient (Patient): The patient receiving treatment.
            treatment (str): Treatment description.

        Returns:
            str: Confirmation message.
        """
        return f"{self.name} prescribed {treatment} to {patient.name}"

    def update_patient_record(self, patient: Patient, new_record: str) -> str:
        """
        Update a patient's medical record.

        Args:
            patient (Patient): The patient whose record is updated.
            new_record (str): The new medical record details.

        Raises:
            ValueError: If the new record is empty.

        Returns:
            str: Confirmation message.
        """
        if not new_record or not new_record.strip():
            raise ValueError("Medical record cannot be empty")
        patient.medical_record = new_record
        return f"Medical record updated for {patient.name}"

    def check_in(self) -> str:
        """Mark the staff member as checked in."""
        return f"{self.name} has checked in."

    def check_out(self) -> str:
        """Mark the staff member as checked out."""
        return f"{self.name} has checked out."
