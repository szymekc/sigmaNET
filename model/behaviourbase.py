from fbchat import Client

class IBehaviourBase(Client):
    """"abstract class being parent of every user implemented behaviour; it handles logging in and tasks on behaviour loader side"""
    def __init__(self, email, password):
        Client.__init__(self, email=email, password=password)

