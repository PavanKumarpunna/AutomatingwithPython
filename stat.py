class student:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def stuname(name):
        return "Hi "+name

print(student.stuname("Virat"))
