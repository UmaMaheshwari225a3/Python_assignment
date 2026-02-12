class Exam:
    pass_marks = 40

    def __init__(self, student_name, total_marks):
        self.student_name = student_name
        self.total_marks = total_marks
        self.score = 0
        self.started = False
        self.submitted = False

    def start_exam(self):
        if not self.started:
            self.started = True
            print(f"Exam started for {self.student_name}")
        else:
            print("Exam already started")

    def submit_exam(self):
        if self.started and not self.submitted:
            self.submitted = True
            print(f"Exam submitted by {self.student_name}")
        else:
            print("Exam not started or already submitted")

    def calculate_score(self, obtained_marks):
        if self.submitted:
            self.score = obtained_marks
            print("Score:", self.score)

            if self.score >= Exam.pass_marks:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Exam not submitted yet")

    @classmethod
    def update_pass_marks(cls, new_pass_marks):
        cls.pass_marks = new_pass_marks
        print("Pass marks updated to:", new_pass_marks)

exam1 = Exam("Uma", 100)
exam1.start_exam()
exam1.submit_exam()
exam1.calculate_score(85)
Exam.update_pass_marks(50)
