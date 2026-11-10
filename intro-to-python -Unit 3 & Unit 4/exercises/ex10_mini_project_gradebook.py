"""Exercise 10 (mini project): a gradebook that uses everything from the session.

Read data/students.csv, work out each student's grade band, and write a report.
Check your work:
    python check.py ex10
Then run it for real:
    python exercises/ex10_mini_project_gradebook.py
"""

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def grade_band(score: int) -> str:
    """Return the grade band for a student's score."""

    if score >= 70:
        return "Distinction"
    elif score >= 60:
        return "Merit"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


def read_students(path: str) -> list[dict]:
    """Read the CSV file and return a list of student dictionaries."""

    students = []

    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "name": row["name"],
                "course": row["course"],
                "score": int(row["score"])
            }

            students.append(student)

    return students


def class_average(students: list[dict]) -> float:
    """Calculate the average score of all students."""

    if not students:
        return 0.0

    total = sum(student["score"] for student in students)

    return round(total / len(students), 1)


def band_counts(students: list[dict]) -> dict[str, int]:
    """Count students in each grade band."""

    counts = {}

    for student in students:
        band = grade_band(student["score"])

        if band in counts:
            counts[band] += 1
        else:
            counts[band] = 1

    return counts


def write_report(students: list[dict], path: str) -> int:
    """Write a CSV report with highest score first."""

    sorted_students = sorted(
        students,
        key=lambda student: student["score"],
        reverse=True
    )

    with open(path, "w", encoding="utf-8", newline="") as file:
        fieldnames = ["name", "score", "band"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in sorted_students:
            writer.writerow({
                "name": student["name"],
                "score": student["score"],
                "band": grade_band(student["score"])
            })

    return len(sorted_students)


def main() -> None:
    """Run the gradebook on data/students.csv and print a summary."""

    students = read_students(str(DATA_DIR / "students.csv"))

    print(f"Students     : {len(students)}")
    print(f"Class average: {class_average(students)}")

    for band, count in band_counts(students).items():
        print(f"  {band:<12} {count}")

    output = DATA_DIR / "output" / "report.csv"
    output.parent.mkdir(parents=True, exist_ok=True)

    written = write_report(students, str(output))

    print(f"Report with {written} students written to {output}")


if __name__ == "__main__":
    main()
