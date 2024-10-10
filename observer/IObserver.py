from abc import ABC, abstractmethod

class IObserver(ABC):
    
    @abstractmethod
    def update(self, delivey_statut):
        pass