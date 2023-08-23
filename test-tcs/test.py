import sys
class stud: 
    'base class for students'
    def __init__(self,rollno,grade):
        self.rollno=rollno;
        self.grade=grade;
    def display(self):
        print(self.rollno,self.grade);
print(stud.__doc__);


print(sys.version)