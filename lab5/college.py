class Student(object):

    def __init__(self, name, course, email_id, status):
        """
        Student object takes 4 arguments - name(str), course(str),
        email_id(str), status(str) - Permitted Values - Active, Inactive
        """

        self.name = name
        self.course = course
        self.email_id = email_id
        self.status = status

    def disable(self):
        self.status = "Inactive"

    def enable(self):
        self.status = "Active"


    def __str__(self):
# return "%s studying in %s - %s" % (self.name, self.course, self.status)
      return "{} studying in {} - {} and email-id is {}".format(self.name, self.course, self.status,self.email_id)



# Tests for the class Student

student1 = Student( course="B.Sc", email_id="murthyraju@college.com",name="Murthy Raju",status= "Active")
student2= Student( "vedha","b.tech","vehda@gmail.com","active")
print(student1)

student1.disable()

print(student1)
print(student2)
