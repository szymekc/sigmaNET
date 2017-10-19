from fbchat import Client
import fbchat
import threading

from model import behaviourbase

class behaviourClass(behaviourbase.IBehaviourBase):

    def SendToSigma(self, message):
        self.sendMessage(message, thread_id=self.CONF_ID, thread_type=fbchat.ThreadType.GROUP)


    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        #dodawaj tylko jezeli czlonek spisku && jezeli czlonek spisku wywalil to nie dodawaj
        #if(removed_id != self.uid and thread_id==CONF_ID and (removed_id in  CONSPIRACY) and (author_id not in CONSPIRACY)):

            self.addQueue.append(removed_id)
            self.SendToSigma("Ej, a to taki dobry człowiek jest :<")
            if(not self.addFlag):
                self.HydraThreads.append(threading.Thread(target=self.addingLoop))
                self.HydraThreads[-1].start()
            self.addFlag =True


            #### usuwanie wykomentowanie dla maksymalizacji rozpaczy
            #Client.removeUserFromGroup(self, user_id=author_id, thread_id=CONF_ID)
        #else:
            #pass



    def addingLoop(self):
        while(self.addQueue.__len__() != 0):
            Client.addUsersToGroup(self, self.addQueue.pop(), self.CONF_ID)

        self.addFlag = False


    def Run(self):
        self.addFlag = False
        self.addQueue=[]
        self.HydraThreads = []
        self.CONF_ID = "1149408855159567"
        self.SendToSigma("HYDREN STARTEN")
        while(True):
            self.listen()
