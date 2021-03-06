import fbchat
import importlib
from model import behaviourbase
from model import loginmanager
import threading

class FbChatManager:
    """class containing all facebook fbchat clients"""
    behaviourClasses=dict()
    ## dictionairy name of module taken from behaviours and moodule imported dynamically

    fbAccounts= loginmanager.LoginManager()
    #class holding and loading fb accounts

    def __init__(self):
        self.activeFbClients=dict()
        self.activeBehaviourThreads=[]
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

        # bind account name with behaviour module engaged with it
        self.activeFbClients.update({ accountName : behaviourClassName })

        # start thread by initializing __init__ of give class and put it into the thread list
        self.activeBehaviourThreads.append(
            threading.Thread(target=self.behaviourClasses[behaviourClassName],
                             kwargs={#"self": self.behaviourClasses[behaviourClassName],
                                     "email": self.fbAccounts.fbLogins[accountName]["email"],
                                     "password": self.fbAccounts.fbLogins[accountName]["password"]}))

        #start this thread [-1] in python gives last element
        self.activeBehaviourThreads[-1].start()


