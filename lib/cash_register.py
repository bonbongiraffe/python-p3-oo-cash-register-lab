#!/usr/bin/env python3

class CashRegister:
  def __init__( self, discount = 0, total = 0 ):
    self.discount = discount
    self.total = total
    self.items = []
    self.transactions = []
  
  def get_discount(self):
    return self._discount 
  
  def set_discount( self, discount ):
    if type(discount) == int:
      self._discount = discount
    else:
      print("discount must be an integer.")
    
  def add_item( self, title, price, quantity = 1 ):
    self.total += price*quantity
    for i in range(quantity):
      self.items.append(title)
    self.transactions.append({"title": title, "price": price, "quantity": quantity})

  def apply_discount( self ):
    if self.discount != 0 :
      self.total *= (100 - self.discount)/100
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction( self ):
    last_transaction = self.transactions[-1]
    for i in range(last_transaction["quantity"]):
      del self.items[-1]
      self.total -= last_transaction["price"]



  discount = property( get_discount, set_discount )
