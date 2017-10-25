class Employee:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience
        description = "List of employees and their year of experience"
        author = "Dipak Dash"
        self.printEmployee()
        
    def printEmployee(self):
        print self.name
        print self.experience

if __name__ == "__main__":
    #emp = Employee("Rohit", 5)
    #emplist = dict()
    #print type(emplist)
    #print dir(emplist)
    emplist = {'Dipak':'8', 'Rohit':'7', 'Rohit1':'3.51'}
    print type(emplist)
    for (k,v) in emplist.iteritems():
        print ("EmpName = %s , Yr of Exp = %f") % (k,round(float(v), 2))
        