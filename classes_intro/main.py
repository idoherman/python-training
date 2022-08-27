class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"name: {self.name} || grade: {self.grade}"

    def factor(self, bonus):
        self.grade += bonus


if __name__ == '__main__':
    st1 = Student("Ido", 100)
    print(st1)
    st1.factor(-3)
    print(st1)
