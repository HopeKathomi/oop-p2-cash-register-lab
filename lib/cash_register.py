
#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        transaction_total = price * quantity

        self.total += transaction_total
        self.items.extend([item] * quantity)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
            "total": transaction_total
        })

    def apply_discount(self):
        if self.discount:
            self.total *= (100 - self.discount) / 100
            print(
                f"After the discount, the total comes to ${self.total:.0f}."
            )
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        self.total -= transaction["total"]

        item = transaction["item"]
        quantity = transaction["quantity"]

        for _ in range(quantity):
            self.items.remove(item)
