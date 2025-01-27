class Human:
    """
    Клас опису людини

    Attributes:
        gender (str): cтать
        age (int): вік
        first_name (str): ім'я
        last_name (str): прізвище
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        """
        Ініціалізує екземпляр класу Human

        Parameters:
            gender (str): стать
            age (int): вік
            first_name (str): ім'я
            last_name (str): прізвище
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Повертає представлення об'єкта Human у str.

        Returns:
            str: інформація про людину
        """
        return f"{self.first_name} {self.last_name}, Вік: {self.age}, {self.gender}"


class Student(Human):
    """
    Клас опису студента, успадкований від класу Human

    Attributes:
        record_book (str): номер студентського квитка
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        """
        Ініціалізує екземпляр класу Student

        Параметри:
            gender (str): стать студента
            age (int): вік студента
            first_name (str): ім'я студента
            last_name (str): прізвище студента
            record_book (str): номер студентського квитка
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Повертає представлення об'єкта Student у str

        Returns:
            str: інформація про студента
        """
        return f"Студент: {super().__str__()}, Студ. виток: {self.record_book}"


class Group:
    """
    Клас опису групи студентів

    Attributes:
        number (str): номер групи
        group (set): студенти які є в групі
    """

    def __init__(self, number: str):
        """
        Ініціалізує екземпляр класу Group

        Parameters:
            number (str): номер групи
        """
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        """
        Додає студента до групи

        Parameters:
            student (Student): об'єкт класу Student, який додається до групи
        """
        self.group.add(student)

    def delete_student(self, last_name: str):
        """
        Видаляє студента з групи за прізвищем

        Parameters:
            last_name (str): прізвище студента, якого потрібно видалити
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        """
        Знаходить студента по прізвищу

        Parameters:
            last_name (str): прізвище студента

        Returns:
            Student | None: об'єкт класу Student - якщо знайдений, або None
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """
        Повертає представлення об'єкта Group у str.

        Returns:
            str: інформація про групу та студентів у ній
        """
        all_students = "\n".join(str(student) for student in self.group)
        return f"Номер групи: {self.number}\nСтуденти:\n{all_students}"


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")

gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)
print(gr)

assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert isinstance(gr.find_student("Jobs"), Student) is True

gr.delete_student("Taylor")
print(gr)

gr.delete_student("Taylor")
