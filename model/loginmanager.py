
class LoginManager:
    def __init__(self, filepath):
        ## dictionairy of dictionairies in the format name of accout: dict(passowrd:x
        self.fbLogins = dict()
        self.login = open(filepath, "r")
    def load(self):
        lines = self.login.readlines()
        for line in lines:
            fields= line.split(" ")
            if len(fields) != 3:
                raise Exception("Invalid number of fields")
            fbname = fields[0]
            fbemail = fields[1]
            fbpassword = fields[2]
            self.fbLogins.update({fbname : {"email":fbemail, "password": fbpassword}})
