from model import FbChatManager

class ImportHydraTest:
    def __init__(self):
        test = FbChatManager.FbChatManager()
        login = open("tests/login.txt", "r")
        fbemail = login.readline()
        fbpassword = login.readline()
        fbname = login.readline()
        test.addFbAccount(fbname, fbemail, fbpassword)
        test.importBehaviour("hydra")
        test.engageBehaviour("hydra", fbname)