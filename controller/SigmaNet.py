from model import FbChatManager
from view import UIManager

class SigmaNet:

    def __init__(self):
        self.FbChatManager= FbChatManager.FbChatManager()
        self.ViewManager= UIManager.UIManager()

    def LoginFromFile(self,filepath):
        """login frrom file"""
        self.FbChatManager.fbAccounts.loadFromFile(filepath)

    def Login(self,name, fbEmail, fbPassword):
        """login single account"""
        self.FbChatManager.fbAccounts.loadSingle(name,fbEmail,fbPassword)


    def DispAccounts(self):
        """list every account login info"""
        print(self.FbChatManager.fbAccounts)
        for account in self.FbChatManager.fbAccounts.fbLogins:
            print("name: " + account)
            for accountDetalis in self.FbChatManager.fbAccounts.fbLogins[account]:
                print(accountDetalis, ':', self.FbChatManager.fbAccounts.fbLogins[account][accountDetalis])

    def DispActiveAccounts(self):
        """list every fb account that sigma is logged in"""
        for client in self.FbChatManager.activeFbClients:
            print("name: "+ client)
            print("behaviour: "+ self.FbChatManager.activeFbClients[client][1])


    def Run(self, fbName, ModuleName):
        self.FbChatManager.importBehaviour(ModuleName)
        self.FbChatManager.engageBehaviour(ModuleName, fbName)

