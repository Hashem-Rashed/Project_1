from person import Person
from patient import Patient
from staff import Staff
from department import Department
from hospital import Hospital

def print_initial_table(hospital):
    """Print departments with staff and patients in table format."""
    print("\n🏥 Initial Hospital Overview\n")
    print(f"{'Department':<15} | {'Staff':<20} | {'Patients':<30}")
    print("-" * 70)
    for dept in hospital.departments:
        staff_names = ", ".join(s.name for s in dept.staff) if dept.staff else "None"
        patient_names = ", ".join(p.name for p in dept.patients) if dept.patients else "None"
        print(f"{dept.name:<15} | {staff_names:<20} | {patient_names:<30}")
    print("-" * 70)

def prefill_hospital(hospital):
    """Add sample departments, staff, and patients for testing."""
    # Departments
    cardio = Department("Cardiology")
    neuro = Department("Neurology")
    hospital.add_department(cardio)
    hospital.add_department(neuro)

    # Staff
    cardio.add_staff(Staff("Dr. Smith", 45, "Cardiologist"))
    cardio.add_staff(Staff("Nurse Jane", 30, "Nurse"))
    neuro.add_staff(Staff("Dr. Lee", 50, "Neurologist"))

    # Patients
    cardio.add_patient(Patient("Alice", 30, "No known allergies"))
    cardio.add_patient(Patient("Bob", 40, "Diabetic"))
    neuro.add_patient(Patient("Carol", 25, "Asthma"))

def main():
    hospital = Hospital("City Hospital", "123 Main St")
    prefill_hospital(hospital)
    print_initial_table(hospital)

    while True:
        print("\n===== HOSPITAL MENU =====")
        print("1. Add Department")
        print("2. Add Staff to Department")
        print("3. Add Patient to Department")
        print("4. Transfer Patient")
        print("5. View Hospital Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter department name: ")
            dept = Department(name)
            hospital.add_department(dept)

        elif choice == "2":
            if not hospital.departments:
                print("No departments yet. Add a department first.")
                continue
            for i, d in enumerate(hospital.departments, 1):
                print(f"{i}. {d.name}")
            dep_index = int(input("Choose department number: ")) - 1
            dep = hospital.departments[dep_index]
            name = input("Staff name: ")
            age = int(input("Staff age: "))
            position = input("Position: ")
            dep.add_staff(Staff(name, age, position))

        elif choice == "3":
            if not hospital.departments:
                print("No departments yet. Add a department first.")
                continue
            for i, d in enumerate(hospital.departments, 1):
                print(f"{i}. {d.name}")
            dep_index = int(input("Choose department number: ")) - 1
            dep = hospital.departments[dep_index]
            name = input("Patient name: ")
            age = int(input("Patient age: "))
            medical_record = input("Medical record: ")
            dep.add_patient(Patient(name, age, medical_record))

        elif choice == "4":
            patient_name = input("Enter patient name to transfer: ")
            from_dep_name = input("From department: ")
            to_dep_name = input("To department: ")
            from_dep = next((d for d in hospital.departments if d.name == from_dep_name), None)
            to_dep = next((d for d in hospital.departments if d.name == to_dep_name), None)
            if from_dep and to_dep:
                patient = next((p for p in from_dep.patients if p.name == patient_name), None)
                if patient:
                    from_dep.patients.remove(patient)
                    to_dep.add_patient(patient)
                    print(f"🚨 Patient Transfer: {patient.name} moved to {to_dep.name}")
                else:
                    print("Patient not found in the source department.")
            else:
                print("Invalid department names.")

        elif choice == "5":
            print_hospital_summary(hospital)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

def print_hospital_summary(hospital):
    """Print full hospital summary."""
    print(f"\n📊 Hospital Summary: {hospital.name}")
    print(f"Location: {hospital.location}")
    total_staff = sum(len(d.staff) for d in hospital.departments)
    total_patients = sum(len(d.patients) for d in hospital.departments)
    print(f"Total Departments: {len(hospital.departments)}")
    print(f"Total Staff: {total_staff}")
    print(f"Total Patients: {total_patients}\n")

    for dept in hospital.departments:
        print(f"🩺 Department: {dept.name}")
        print(f"  Staff ({len(dept.staff)}):")
        for s in dept.staff:
            print(f"    - {s.name}, {s.position}, Age: {s.age}")
        print(f"  Patients ({len(dept.patients)}):")
        for p in dept.patients:
            print(f"    - {p.name}, Age: {p.age}")
            print(f"      Medical Record: {p.medical_record}")
        print("-" * 50)

if __name__ == "__main__":
    main()
