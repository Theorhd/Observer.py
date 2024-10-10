from observer.IObserver import IObserver

class User(IObserver):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def update(self, delivery_status):
        print(f"Email envoyé à {self.email} : La commande est maintenant {delivery_status}")