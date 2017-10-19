from model import FbChatManager
from view import UIManager

class SigmaNet:

    def __init__(self):
        self.FbChatManager= FbChatManager.FbChatManager()
        self.ViewManager= UIManager.UIManager()

    def Login(self,name,email,password):
        #login single account
        self.FbChatManager.fbAccounts.load()

    def Accounts(self):
        """list every account login info"""
        print(self.FbChatManager.fbAccounts)

    def ActiveAccounts(self):
        """list every fb account that sigma is logged in"""
        for client in self.FbChatManager.activeFbClients:
            print("name: "+ client)
            print("behaviour: "+ self.FbChatManager.activeFbClients[client][1])

