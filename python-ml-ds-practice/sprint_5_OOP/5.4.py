class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:

    def __init__(self):
        self.tests_taken = 'No tests taken'
    def take_test(self, testpaper: Testpaper, answers):
        if self.tests_taken == 'No tests taken' :
            self.tests_taken = dict()

        correct_answers = 0
        for i, answer in enumerate(answers):
            if answer == testpaper.markscheme[i]: correct_answers += 1

        total_questions = len(testpaper.markscheme)
        percentage = round((correct_answers / total_questions) * 100)

        passed = percentage >= int(testpaper.pass_mark.strip("%"))
        result = "Passed!" if passed else "Failed!"
        self.tests_taken[testpaper.subject] = f"{result} ({percentage}%)"

paper1 = Testpaper('Maths', ['1A', '2C', '3D', '4A', '5A'], '60%')
paper3 = Testpaper('Computing', ['1D', '2C', '3C', '4B', '5D', '6C', '7A'], '75%')

student2 = Student()
student3 = Student()

student2.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)

student3.take_test(paper1, ['1C', '2D', '3A', '4C', '5A'])
student3.take_test(paper3, ['1A', '2C', '3A', '4C', '5D', '6C', '7B'])
print(student3.tests_taken)
print(paper3.subject)
print(paper3.markscheme)
print(paper3.pass_mark)