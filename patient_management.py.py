"""
Hospital Patient Management
Search patients by disease
"""

def search_by_disease(patients, disease):
    result = []
    for patient in patients:
        if patient["Disease"].lower() == disease.lower():
            result.append(patient["Name"])
    return result


# Example Run
if __name__ == "__main__":
    patients = [
        {"Name": "Alice", "Age": 30, "Disease": "Flu"},
        {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
        {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
    ]

    search_disease = "Flu"
    found = search_by_disease(patients, search_disease)

    print(f"Patients with {search_disease}: {found}")
