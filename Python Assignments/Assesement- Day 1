##### QUESTION 1:    Write a Python class to convert an integer to a Roman numeral.

class RomanNumerals:
    def Roman(self, num):
        numToRoman = {1: "I",5: "V",4: "IV", 10: "X",9: "IX",50: "L",   40: "XL",100: "C",  90: "XC",500: "D",  400: "CD",1000: "M", 900: "CM",}
        
        r = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                r += numToRoman[n]
                num-=n
        print(r)



##### QUESTION 2: Write a Python class to get all possible unique subsets from a set of distinct integers.
Input : [4, 5, 6]

class unique_subset:
    def sub_sets(self, subset):
        return self.subsets_Recur([], sorted(subset))
    
    def subsets_Recur(self, current, sset):
        if sset:
            return self.subsets_Recur(current, sset[1:]) + self.subsets_Recur(current + [sset[0]], sset[1:])
        return [current]

print(unique_subset().sub_sets([4,5,6]))





###### QUESTION 3: Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of 
########           the class. Now remove the student_name attribute and display the entire attribute with values.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("**************************************")
        attributes = vars(self)
        for k, v in attributes.items():
            print(f"{k}: {v}")

    def add_attribute(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)

    def remove_attribute(self, attr_name):
        delattr(self, attr_name)


student1 = Student(2674, "Syam")
student1.add_attribute("student_city", "Vizag")
student1.display_attributes()
student1.remove_attribute("student_name")
student1.display_attributes()


