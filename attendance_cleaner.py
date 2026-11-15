from pathlib import Path

INPUT_FILE = "attendance.txt"
OUTPUT_FILE = "attendance_clean.csv"


def clean_attendance():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            original_names = file.readlines()

    except FileNotFoundError:
        print(f"Error: '{INPUT_FILE}' was not found.")
        print("Create the file and add one student name per line.")
        return

    # Clean extra spaces and capitalization. Ignore blank lines.
    cleaned_names = [
        name.strip().title()
        for name in original_names
        if name.strip()
    ]

    # A set removes repeated names.
    unique_names = set(cleaned_names)

    # Convert the set back to a list and sort alphabetically.
    sorted_names = sorted(unique_names)

    # Save the cleaned names as one name per row in a CSV file.
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as file:
        file.write("student_name\n")
        for name in sorted_names:
            file.write(f'"{name}"\n')

    print("\n--- Attendance Cleaning Report ---")
    print(f"Original number of records: {len(original_names)}")
    print(f"Unique student count: {len(unique_names)}")
    print("\nCleaned attendance list:")

    if sorted_names:
        for number, name in enumerate(sorted_names, start=1):
            print(f"{number}. {name}")
    else:
        print("No student names were found.")

    print(f"\nCleaned attendance saved to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    clean_attendance()
