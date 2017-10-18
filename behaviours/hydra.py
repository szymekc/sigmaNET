from fbchat import Client
import fbchat
import threading

from model import behaviourbase

SUBJECT_ID="100009816161880"
CONF_ID="1673360209355525"
CONSPIRACY=["100007142767580","100006193238725", "100005032903512","100006245283330","100016113762090"]

class HydraKeeper(behaviourbase.IBehaviourBase):
    addFlag=False
    addQueue=[] #lista osob ktore maja zostc dodane

    #watki na petle oczekujace
    HydraThreads=[]


    #uproszczona funkcja wysylania wiwaomosci
    def SendToSigma(self, message):
        self.sendMessage(message, thread_id=CONF_ID, thread_type=fbchat.ThreadType.GROUP)


    def onPersonRemoved(self, removed_id, author_id, thread_id, **kwargs):
        #dodawaj tylko jezeli czlonek spisku && jezeli czlonek spisku wywalil to nie dodawaj
        #if(removed_id != self.uid and thread_id==CONF_ID and (removed_id in  CONSPIRACY) and (author_id not in CONSPIRACY)):
            self.addQueue.append(removed_id)
            if(not self.addFlag):
                self.HydraThreads.append(threading.Thread(target=self.addingLoop))
                self.HydraThreads[-1].start()
            self.addFlag =True

            #### usuwanie wykomentowanie dla maksymalizacji rozpaczy
            #Client.removeUserFromGroup(self, user_id=author_id, thread_id=CONF_ID)
        #else:
            #pass



    def addingLoop(self):
        for person in self.addQueue:
            Client.addUsersToGroup(self, person, CONF_ID)


