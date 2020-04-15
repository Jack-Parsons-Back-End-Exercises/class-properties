class Student():

    @property
    def firstName(self):
        try:
            return self.__firstName
        except AttributeError:
            return 0

    @firstName.setter
    def firstName(self, new_firstName):
        if type(new_firstName) is str:
            self.__firstName = new_firstName
        else:
            raise TypeError("firstName must be a string")

    @property
    def lastName(self):
        try:
            return self.__lastName
        except AttributeError:
            return 0

    @lastName.setter
    def lastName(self, new_lastName):
        if type(new_lastName) is str:
            self.__lastName = new_lastName
        else:
            raise TypeError("lastName must be a string")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    
    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("age must be an int")

    @property
    def cohortNum(self):
        try:
            return self.__cohortNum
        except AttributeError:
            return 0

    @cohortNum.setter
    def cohortNum(self, new_cohortNum):
        if type(new_cohortNum) is int:
            self.__cohortNum = new_cohortNum
        else:
            raise TypeError("cohortNum must be an int")

    @property
    def fullName(self):
        try:
            return f'{self.firstName} {self.lastName}'
        except AttributeError:
            return 0
        

kyle = Student()
kyle.firstName = "Kyle"
kyle.lastName = "Murphy"
kyle.cohortNum = 29

print(kyle.fullName)