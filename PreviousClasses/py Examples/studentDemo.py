

from student import Student

def studentDemo():
    student1=Student("John","A","Doe",23,4.0,"Ames",True)
    print student1.getName()
    print student1.getGPA()
    student1.modifyGPA(3.66)
    print student1.getGPA()
    print student1.hasHold()

    student2=Student("John","A","Doe",23,4.0,"Ames",True)
    student3=Student("John","B","Doe",23,4.0,"Ames",True)
    print 
    print "Equality Test #1"
    print str(student1) +"=="+ str(student2)
    print (student1==student2)
    print 
    print "Equality Test #2"
    print str(student2) +"=="+ str(student3)
    print (student1==student3)
    print 
    print "Inequality Test"
    print str(student1) +"<"+ str(student3)
    print (student1<student3)
