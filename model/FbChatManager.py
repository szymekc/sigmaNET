import fbchat
import importlib
from model import behaviourbase
from model import loginmanager
class FbChatManager:
    """class containing all facebook fbchat clients"""
    behaviourClasses=dict()
    ## dictionairy name of module taken from behaviours and moodule imported dynamically

    fbAccounts= loginmanager.LoginManager("tests/login.txt")
    #class holding and loading fb accounts
    
    def __init__(self):
        self.activeFbClients=dict()
        # dict of active fb client in form (name: {fbclient, behaviourclass})

    def importBehaviour(self, className):
        behaviourModule= importlib.import_module("behaviours."+className)
        # load module of given name from behaviours
        behaviourClass = getattr(behaviourModule, "behaviourClass")
        # getattr loads class from given module

        self.behaviourClasses.update({className:behaviourClass})

    def engageBehaviour(self, behaviourClassName, accountName):
        """turn behaviour class on"""
        #check if account name exist in dict
        if( not accountName in self.fbAccounts.fbLogins):
            raise Exception("no given account name found")

        #check if given behaviour class is loaded
        if(not behaviourClassName in self.behaviourClasses):
            raise Exception("no given behaviour class")

        facebookClient=  self.__CreateNewFbClient(self, self.fbAccounts.fbLogins[accountName]["email"],
                                                  self.fbAccounts.fbLogins[accountName]["password"],
                                                  self.behaviourClasses[behaviourClassName])
        self.activeFbClients.update({ accountName : {facebookClient,behaviourClassName} })


    def ___CreateNewFbClient(self, email, password, className):
        #append clients by initializing behaviour class given by className keyed from modules dict
        self.fbchatClients.append(
            self.behaviourClasses[className](email, password))

