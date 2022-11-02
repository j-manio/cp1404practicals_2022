class ProgrammingLanguage:
    def __init__(self, name="", is_dynamic=False, is_reflection=False, year=0):
        self.name = name
        self.is_dynamic = is_dynamic
        self.reflection = is_reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.is_dynamic}, Reflection={self.reflection}, First appeared in {self.year}"