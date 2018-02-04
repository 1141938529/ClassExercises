class personMessage():
    def __init__(self, name, tel, qq, email,adress):
        self.name = name
        self.tel = tel
        self.qq = qq
        self.adress = adress
        self.email = email
        pass
    def __str__(self):
        return "personMessage: name="+self.name+",tel="\
               +self.tel+",qq="+self.qq+",email="+self.email+",aderess="+self.adress
