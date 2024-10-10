from delivery.delivery import Delivery
from user.user import User

def main():
    
    delivery = Delivery("1234ABC")
    print(f"Le numéro de suivi de la commande est : {delivery.get_tracking_number()}")
    
    
    user_Theo = User("Théo", "contact@theorichard.fr")
    user_Marie = User("Marie", "contact@marie.fr")
    
    delivery.attach(user_Theo)
    delivery.attach(user_Marie)
    
    delivery.change_status("En cours de préparation")
    delivery.change_status("En cours de livraison")
    delivery.change_status("Livrée")
    
    
if __name__ == "__main__":
    main()