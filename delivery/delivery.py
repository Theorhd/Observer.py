from observer.ISubject import ISubject

class Delivery(ISubject):
    
    def __init__(self, tracking_number):
        self._tracking_number = tracking_number
        self.status = "Commande recue"
        self.observers = []
        
    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print("Un éléments renseigné n'est pas dans la liste des observateurs")
    
    def notify(self):
        for observer in self.observers:
            observer.update(self.status)
            
    def change_status(self, new_status):
        self.status = new_status
        self.notify()
        
    def get_status(self):
        return self.status
    
    def get_tracking_number(self):
        return self._tracking_number