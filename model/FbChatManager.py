import fbchat
import importlib
from model import behaviourbase

class FbChatManager:
    """class containing all facebook fbchat clients"""
    behaviourClasses=dict()
    ## dictionairy name of module taken from behaviours and moodule imported dynamically

    fbAccounts= dict()
    ## dictionairy of dictionairies in the format name of accout: dict(passowrd:x, email:y)

    def __init__(self):
        self.fbchatClients=[]


    def addFbAccount(self,name , email, password):
        #add facebook account
        self.fbAccounts.update({name: dict({"email": email,"password": password})})

    def importBehaviour(self, className):
        behaviourModule= importlib.import_module("behaviours."+className)
        # load module of given name from behaviours
        behaviourClass = getattr(behaviourModule, "behaviourClass")
        # getattr loads class from given module

        self.behaviourClasses.update({className:behaviourClass})

    def engageBehaviour(self, behaviourClassName, accountName):
        """turn behaviour class on"""
        #check if account name exist in dict
        if( not accountName in self.fbAccounts):
            raise Exception("no given account name found")

        #check if given behaviour class is loaded
        if(not behaviourClassName in self.behaviourClasses):
            raise Exception("no given behaviour class")

        facebookClient=  self.behaviourClasses[behaviourClassName](
            self.fbAccounts[accountName]["email"],
            self.fbAccounts[accountName]["password"]
        )



    def ___CreateNewFbClient(self, email, password, className):
        #append clients by initializing behaviour class given by className keyed from modules dict
        self.fbchatClients.append(
            self.behaviourClasses[className](email, password))