class AccountInfo:
    def _init_(self, username, password, first, last, phone, email, str_num, str_name, city, province, postal_code):
        self.username = username
        self.password = password
        self.name = [first, last]
        self.phone = phone
        self.email = email
        self.address = [str_num, str_name, city, province, postal_code]


    @property
    def username(self):
        return self.username
    
    @username.setter
    def username(self, value):
        self.username = value

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, value):
        self.password = value

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, first, last):
        self.name = [first, last]

    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def phone(self, value):
        self.phone = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        self.email = value
    
    @property
    def address(self):
        return self.address 
    
    @address.setter
    def address(self, str_num, str_name, city, province, postal_code):
        self.address = [str_num, str_name, city, province, postal_code]


    

        