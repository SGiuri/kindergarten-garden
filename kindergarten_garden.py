class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"]

        self.plants_varieties = {"R": "Radishes",
                                 "G": "Grass",
                                 "C": "Clover",
                                 "V": "Violets"}

        self.first_row_diagram = diagram.split()[0]
        self.second_row_diagram = diagram.split()[1]
        if len(self.first_row_diagram) != len(self.second_row_diagram):
            raise Exception("Some kid will miss his plant!")

        self.students = students
        self.students.sort()

    def plants(self, student):
        if student in self.students:
            self.student_index = self.students.index(student)

            self.student_plants_indexes = self.student_index * 2, self.student_index * 2 + 1
            student_plants_1 = self.first_row_diagram[
                               self.student_plants_indexes[0]:self.student_plants_indexes[1] + 1]
            student_plants_2 = self.second_row_diagram[
                               self.student_plants_indexes[0]:self.student_plants_indexes[1] + 1]
            student_plants = student_plants_1 + student_plants_2

        return [self.plants_varieties[j] for j in student_plants]
