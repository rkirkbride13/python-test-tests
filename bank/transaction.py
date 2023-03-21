import datetime

class Transaction:

  def __init__(self, amount, date = datetime.datetime.now()):
    self.amount = amount
    self.date = date

  def format_amount(self):
    if self.amount > 0:
      return f"{self.amount}.00 ||"
    else:
      return f"|| {-self.amount}.00"
  
  def format_date(self):
    return self.date.strftime("%d/%m/%Y")
  
