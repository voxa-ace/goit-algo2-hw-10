# Define the Teacher class
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"  # For debugging purposes

# Function to create a schedule using a greedy algorithm
def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        # Sort teachers by the number of uncovered subjects they can teach, and by age
        teachers.sort(key=lambda t: (-len(t.can_teach_subjects & remaining_subjects), t.age))
        
        # Select the best teacher
        best_teacher = teachers[0]
        covered_subjects = best_teacher.can_teach_subjects & remaining_subjects

        if not covered_subjects:
            return None  # It's impossible to cover all subjects

        # Assign subjects to the selected teacher
        best_teacher.assigned_subjects = covered_subjects
        remaining_subjects -= covered_subjects
        schedule.append(best_teacher)

    return schedule

if __name__ == '__main__':
    # Define the set of subjects
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Create the list of teachers
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Create the schedule
    schedule = create_schedule(subjects, teachers)

    # Output the schedule
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
