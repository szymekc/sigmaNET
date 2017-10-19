
class LoginManager:

    def __init__(self):
        ## dictionairy of dictionairies in the format name of accout: dict(passowrd:x
        self.fbLogins = dict()

    def loadSingle(self,name, fbEmail, fbPassword):
        """load single account into logins"""
        self.fbLogins.update({name : {"email":fbEmail, "password": fbPassword}})

    def loadFromFile(self,filepath):
        """load accounts from file"""
        login= open(filepath,"r")

        lines = login.readlines()
        for line in lines:
            fields= line.split(" ")
            if len(fields) != 3:
                raise Exception("Invalid number of fields")
            fbname = fields[0]
            fbemail = fields[1]
            fbpassword = fields[2]
            self.fbLogins.update({fbname : {"email":fbemail, "password": fbpassword}})

        login.close()