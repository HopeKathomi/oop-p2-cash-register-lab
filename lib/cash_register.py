#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total =0 ):
    self.discount =int(input("enter discount: "))
    self.total = total
    self.items = []
    self.previous_transactions =[]

  @property
  def Discount(self):
    self.discount = int(self.discount)
    if self.discount >=0 and self.discount <=100:
      return self.discount
    else:
      print("Not valid discount")

  def add_item(self,item, price, quantity):
    self.total += price
    self.items.append(item)
    self.previous_transactions.append({"item": item, "price":price, "quantity":quantity}) 

  def apply_discount(self):
    self.previous_transactions.pop()
    if self.previous_transactions:
      print("There is no discount to apply.")

c = CashRegister(10,10000)
c.Discount
c.add_item("c", 500, 2)
print(c.previous_transactions)