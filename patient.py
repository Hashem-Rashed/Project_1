from person import Person

class Patient(Person):
    """
    Class representing a hospital patient.

    This class extends the Person class by adding medical record information
    specific to patients. It is used to store and manage patient-related data
    in the hospital system.

    Attributes:
        medical_record (str): The patient's medical record.
            Cannot be empty.
    """

    def __init__(self, name, age, medical_record):
        """
        Initialize a Patient object.

        Args:
            name (str): The full name of the patient.
            age (int): The age of the patient.
            medical_record (str): The patient's medical record.

        Raises:
            ValueError: If the medical record is empty.
        """
        super().__init__(name, age)
        if not medical_record or not medical_record.strip():
            raise ValueError("Medical record cannot be empty")
        self.medical_record = medical_record

    def __str__(self):
        """
        Return a user-friendly string representation of the patient.

        Returns:
            str: A readable string including name, age, and medical record.
        """
        return f"{super().__str__()}, Medical Record: {self.medical_record}"

    def __repr__(self):
        """
        Return a detailed string representation of the patient for debugging.

        Returns:
            str: Developer-friendly string including name, age, and medical record.
        """
        return (
            f"Patient(name={self.name!r}, "
            f"age={self.age}, "
            f"medical_record={self.medical_record!r})"
        )

    def view_record(self):
        """
        View the patient's medical record.

        Returns:
            str: A formatted string containing the patient's medical record information.
        """
        return f"Medical Record for {self.name}: {self.medical_record}"

    def update_record(self, new_record):
        """
        Update the patient's medical record.

        Args:
            new_record (str): The new medical record information.

        Raises:
            ValueError: If the new record is empty.

        Returns:
            str: Confirmation message.
        """
        if not new_record or not new_record.strip():
            raise ValueError("Medical record cannot be empty")
        self.medical_record = new_record
        return f"Medical record updated for {self.name}"

    def check_in(self):
        """
        Mark the patient as checked in.

        Returns:
            str: Confirmation message.
        """
        return f"{self.name} has checked in."

    def check_out(self):
        """
        Mark the patient as checked out.

        Returns:
            str: Confirmation message.
        """
        return f"{self.name} has checked out."

    def summary(self):
        """
        Return a summary of patient information.

        Returns:
            str: Name, age, and medical record.
        """
        return f"Patient: {self.name}, Age: {self.age}, Medical Record: {self.medical_record}"
