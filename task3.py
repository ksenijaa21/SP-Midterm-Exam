class Person():

    def __init__(self, name, surname, dob, address):
        self.name = name
        self.surname = surname
        self.dob = dob
        self.address = address

    def __str__(self):
        return "Hello, my name is {0} {1}".format(self.name, self.surname)


class Employee(Person):

    num_of_employees = 0

    def __init__(self, name, surname, dob, address, company, position, years_employed, base_salary):
        Person.__init__(self, name, surname, dob, address)
        self.company = company
        self.position = position
        self.years_employed = years_employed
        self.base_salary = base_salary
        Employee.num_of_employees +=1

    def __str__(self):
        return "Hello, I work at {0} as {1}".format(self.company,self.position)

    def get_salary(self):

        actual_salary = ((int(self.base_salary))*(int(self.years_employed)/100)) + int(self.base_salary)
        return actual_salary

    def get_tax(self):

        tax = (self.get_salary)*(70/100)
        return tax


class Freelancer(Person):

    skills = ['word', 'excel', 'python', 'java']
    reviews = [1, 2, 3, 4, 5]


    def __init__(self, name, surname, dob, address, skills, reviews):
        Person.__init__(self, name, surname, dob, address)
        self.skills = skills
        self.reviews = reviews

    def get_ratings(self, reviews):

        num_of_rev = 0
        sum_of_rev = 0

        x = input()
        if x in reviews:
            num_of_rev +=1
            sum_of_rev += int(x)

        average_rat = int(sum_of_rev) / int(num_of_rev)

        return average_rat


    def __str__(self):
        return "My skill set is {0} and my average rating is {1}".format(self.skills,self.get_ratings())


