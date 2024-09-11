#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.total=0
    self.discount = discount
    self.items =[]
    self.prices =[]

  def reset_register_totals(self):
    return self.total

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(title)
      self.prices.append(price)

  def apply_discount(self):
    self.total = self.total * (1 - self.discount / 100)
    if self.total:
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    if self.items:
        last_item = self.items[-1]
        last_price = self.prices[-1]
        count = self.items.count(last_item)
        for _ in range(count):
            self.items.pop()
            self.prices.pop()
            self.total -= last_price

    
