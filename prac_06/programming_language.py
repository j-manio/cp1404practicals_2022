class ProgrammingLanguage:
    def __init__(self, name="", typing="", is_reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = is_reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic".title()
