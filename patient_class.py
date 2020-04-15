class Patient():

    def __init__(self, ssNumber, dateOfBirth, accountNum, firstName, lastName, address):
        self.__ssNumber = ssNumber
        self.__dateOfBirth = dateOfBirth
        self.__accountNum = accountNum
        self.__firstName = firstName
        self.__lastName = lastName
        self.address = address

    @property
    def ssNumber(self):
        try:
            return self.__ssNumber
        except AttributeError:
            return 0

    @property
    def dateOfBirth(self):
        try:
            return self.__dateOfBirth
        except AttributeError:
            return 0

    @property
    def accountNum(self):
        try:
            return self.__accountNum
        except AttributeError:
            return 0

    @property
    def fullName(self):
        try:
            return f'{self.__firstName} {self.__lastName}'
        except AttributeError:
            return 0

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Address must be a string!')