from student import Student
from university import University

def main():
    tech_university = University("Tech Innovation University")

    Maksud = Student("Maksud", "Temel", "maks.@gmail.com")
    Aziz = Student("Aziz", "Tolibaev", "aziz@gmail.com")

    Maksud.apply_to_university(tech_university, "Computer Science")
    Aziz.apply_to_university(tech_university, "Data Science")

    tech_university.communication_queue.process_events()

if __name__ == "__main__":
    main()
