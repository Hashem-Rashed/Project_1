# hospital_system/__init__.py

from .core import Hospital, Department
from .models import Person, Patient, Staff

__all__ = ["Hospital", "Department", "Person", "Patient", "Staff"]
