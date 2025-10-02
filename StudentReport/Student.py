class Student:
    def __init__(self,name):
        self.name=name
        self.marks={}
    
    def add_subject(self,subject,mark):
        if 0<=mark<=100:
            self.marks[subject]=mark
        else:
            print("Invalid marks. Please enter marks in range 0 to 100")
    
    def calculate_average(self):
        if not self.marks:
            return 0
        total=sum(self.marks.values())
        return total/len(self.marks)
    
    def get_grade(self):
        avg = self.calculate_average()  # ✅ Fix is here
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"
    
    def print_report_card(self):
        print(f"\nReport card for {self.name}")          
        print("-"*30)
        if not self.marks:
            print("No subjects added yet")
            return

        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        
        avg = self.calculate_average()
        grade = self.get_grade()
        print(f"\nAverage Marks: {avg:.2f}")
        print(f"Grade: {grade}")
        print("-" * 30)

def main():
    print("Welcome to the Student Report Card System!")
    student_name = input("Enter student's name: ")
    student = Student(student_name)

    while True:
        print("\nOptions:")
        print("1. Add/Update subject and marks")
        print("2. Show report card")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice=="1":
            subject=input("Enter subject name")
            try:
                mark=float(input("Enter marks (0-100) "))
            except ValueError:
                print("Invalid input.Please enter numeric marks.")
                continue
            student.add_subject(subject, mark)

        elif choice=="2":
            student.print_report_card()
        
        elif choice=="3":
            print("Exiting from the system ")
            break

        else:
            print("Invalid choice")

if __name__=="__main__":
    main()

        

            