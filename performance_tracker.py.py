"""
Classroom Performance Tracker
Calculates average and finds top performer
"""

def calculate_averages(students: dict):
    averages = {}
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        averages[name] = round(avg, 2)
    return averages


def top_performer(averages: dict):
    return max(averages, key=averages.get)


# Example Run
if __name__ == "__main__":
    students = {
        "John": [85, 78, 92],
        "Alice": [88, 79, 95],
        "Bob": [70, 75, 80]
    }

    averages = calculate_averages(students)
    topper = top_performer(averages)

    print("Average Marks:", averages)
    print("Top Performer:", topper)
