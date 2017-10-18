import fbchat
import importlib
from model import behaviourbase

class FbChatManager:
    """class containing all facebook fbchat clients"""
    behaviourModules=dict()
    ## dictionairy name of module taken from behaviours and moodule imported dynamically

    fbAccounts= dict()
    ## dictionairy of dictionairies in the format name of accout: dict(passowrd:x, email:y)

    def __init__(self):
        self.fbchatClients=[]



    def importBehaviour(self, className):
        behaviourModule= importlib.__import__("behaviours."+className)
        self.behaviourModules.update({className:behaviourModule})

    def addFbAccount(self,name , email, password):
        #add facebook account
        self.fbAccounts.update({name: dict({"email": email,"password": password})})

    def ___CreateNewFbClient(self, email, password, className):
        #append clients by initializing behaviour class given by className keyed from modules dict
        self.fbchatClients.append(
            self.behaviourModules[className](email, password))


    def engageBehaviour(self, behaviourClassName, accountName):
        """turn behaviour class on"""
        #check if account name exist in dict
        if( not accountName in self.fbAccounts):
            raise Exception("no given account name found")

        #check if given behaviour class is loaded
        if(not behaviourClassName in self.behaviourModules):
            raise Exception("no given behaviour class")

        facebookClient=  self.behaviourModules[behaviourClassName].HydraKeeper(
            self.fbAccounts[accountName]["email"],
            self.fbAccounts[accountName]["password"]
        )

