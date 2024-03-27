import numpy as np
from tabulate import tabulate


class Main:

    def __init__(self):
        self.first_names = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა', 'ედუარდ', 'კლარა', 'სიმონ',
                            'ანზორ',
                            'სოფია', 'სოსო', 'ნელი', 'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა',
                            'იზოლდა',
                            'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა', 'როზა', 'რუსუდან', 'სიმონ', 'ნელი',
                            'ბადრი',
                            'მადონა', 'ირინე', 'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა',
                            'ნინელი',
                            'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან']

        self.last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია', 'კევლიშვილი', 'ბუჩუკური',
                           'ტყებუჩავა',
                           'მიქაბერიძე', 'ურუშაძე', 'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე',
                           'ღურწკაია',
                           'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი',
                           'კაკაბაძე',
                           'მერებაშვილი',
                           'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი', 'მამულაშვილი', 'ჯოჯუა',
                           'გულუა',
                           'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე', 'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი',
                           'იობიძე', 'გაბაიძე',
                           'ხარაბაძე', 'ინასარიძე', 'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი']

        self.subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ისტორია', 'ქიმია', 'ბიოლოგია']

        self.num_students = 100
        # Create a table with random grades
        self.grades = np.random.randint(1, 101, size=(self.num_students, len(self.subjects)))

        # Add names and surnames to the table
        self.names = [(f"{self.first_names[i % len(self.first_names)]} "
                       f"{self.last_names[i % len(self.last_names)]}") for i in range(self.num_students)]
        self.table = np.column_stack((self.names, self.grades))

        # Add subject names as the first row
        self.table = np.row_stack((["სახელები/საგნები "] + self.subjects, self.table))

    def print_table(self):
        table_list = self.table.tolist()
        print(tabulate(table_list, headers='firstrow', tablefmt='grid'))

    def find_highest_average_student(self):
        student_grades = self.table[1:, 1:].astype(int)
        student_averages = np.mean(student_grades, axis=1)
        highest_average_index = np.argmax(student_averages)
        highest_average_student = self.table[highest_average_index + 1, 0]
        highest_average_score = student_averages[highest_average_index]
        print(f"სტუდენტი ყველაზე მაღალი საშუალო ქულით მათემატიკაში არის {highest_average_student}, "
              f"საშუალო ქულით {highest_average_score:.2f}")

    def find_highest_lowest_math_score(self):
        math_scores = self.table[1:, 2].astype(int)
        highest_math_index = np.argmax(math_scores)
        highest_math_student = self.table[highest_math_index + 1, 0]
        highest_math_score = math_scores[highest_math_index]
        lowest_math_index = np.argmin(math_scores)
        lowest_math_student = self.table[lowest_math_index + 1, 0]
        lowest_math_score = math_scores[lowest_math_index]
        print(f"სტუდენტი ყველაზე მაღალი ქულით მათემატიკაში არის {highest_math_student}, {highest_math_score} ქულით")
        print(f"სტუდენტი ყველაზე დაბალი ქულით მათემატიკაში არის {lowest_math_student}, {lowest_math_score} ქულით")

    def print_students_above_avg_english(self):
        english_scores = self.table[1:, 3].astype(int)
        avg_english_score = np.mean(english_scores)
        above_avg_indices = np.argwhere(english_scores > avg_english_score).reshape(-1) + 1
        above_avg_students = self.table[above_avg_indices, 0]
        print(f"სტუდენტები საშუალო მაღალი ქულით ინგლისურში ({avg_english_score:.2f}):")
        for student in above_avg_students:
            print(student)

    def main(self):
        self.print_table()
        self.find_highest_average_student()
        self.find_highest_lowest_math_score()
        self.print_students_above_avg_english()


if __name__ == '__main__':
    main = Main()
    main.main()
