
class Food:
    def __init__(self):
        self.menu = {
            "idly": [50, 100],
            "dosa": [80, 30],
            "sallad": [120, 60],
            "poori": [30, 30],
            "pongal": [50, 40],
            "parota": [20, 50],
            "vadai": [10, 100]
        }
        self.order = {}

    def display_menu(self):
        for dish, price in self.menu.items():
            print(f"Dish : {dish} - {price[0]}  (Qty : {price[1]})")

    def add_items(self, item, quantity):
        if item in self.menu:
            if item in self.order:
                self.order[item] = self.order[item] + quantity
            else:
                self.order[item] = quantity
        else:
            print("Invalid order")

    def view_orders(self):
        print('***Your order details***')
        total = 0
        for item, quantity in self.order.items():
            if item in self.menu:
                item_price=self.menu[item][0]
                item_total= item_price * quantity
                total=total + item_total
                print(f'{item} X {quantity} : {item_total}')
        print(f'Total : {total}')


def main_page():
    system = Food()
    while True:
        print("1. Display Menu")
        print("2. Add Items")
        print("3. View Orders")
        print("4. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            system.display_menu()
        elif option == 2:
            item = input("Enter the food name: ").lower()
            quantity = int(input("Enter the quantity: "))
            system.add_items(item, quantity)
        elif option == 3:
            system.view_orders()
        elif option == 4:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")


main_page()
