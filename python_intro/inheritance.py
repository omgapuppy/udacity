class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self. eye_color = eye_color

    def show_info(self):
        print("Surname: " + self.last_name)
        print("Eyes: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

# Creating instances in class file ONLY for demo
billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
