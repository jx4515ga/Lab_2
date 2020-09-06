# Importing dataclass
from dataclasses import dataclass

# using the dataclass decorator 
@dataclass

# Creating class sturdent
class Student:

    # Descrining the ariables and their datatypes   
    name: str
    college_id: int
    gpa: float

  # Adding students with their Name, College ID and GPA
def main():

    jess = Student('Jessica', 45135, 4.0)
    mike = Student('Michael', 12345, 3.5)
    jess = Student('Jessica', 45135, 4.0)
    joe = Student('Joseph', 85475, 3.1)
    holly = Student('Holly', 854298, 3.5)

# Printing the variables 
    print(mike)
    print(jess)
    print(joe)
    print(holly)

main()