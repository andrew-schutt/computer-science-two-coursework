class Student:

    def __init__(self,first,middle,last,age,gpa,hometown,hold):
        self.first=first
        self.middle=middle
        self.last=last
        self.age=age
        self.gpa=gpa
        self.hometown=hometown
        self.hold=hold

    def getName(self):
        return self.first+" "+self.middle+" "+self.last

    def getAge(self):
        return self.age

    def getGPA(self):
        return self.gpa

    def modifyGPA(self,newGPA):
        self.gpa=newGPA

    def hasHold(self):
        return self.hold

    def __str__(self):
        return "[ "+self.getName()+", "+str(self.gpa)+", hold="+str(self.hold)+"]"

    def __cmp__(self,other):
        if self.getName()==other.getName():
            return 0
        elif self.getName()<other.getName():
            return -1
        else:
            return 1
