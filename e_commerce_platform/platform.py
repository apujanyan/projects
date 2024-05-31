from order_operations import OrderOperation


class Platform(OrderOperation):
    def __init__(self) -> None:
        self.orders = []

    def deliver_order(self, order) -> None:
        if order in self.orders:
            self.orders.pop(order)
            print(f'Order {order.name} is delivered. ')
            return
        print(f'No order {order.name} in orders\' list')




