from rich.console import Console
from rich.table import Table

def catalog():
  print("Online Store")
  print("----------------")
  
  table = Table(title="Product Catalog")
  
  item1, item2, item3 = 200, 400, 600
  
  combo1 = (90/100)*(item1 + item2)
  combo2 = (90/100)*(item2 + item3)
  combo3 = (90/100)*(item1 + item3)
  combo4 = (75/100)*(item1 + item2 + item3)
  
  rows = [
    ["Item 1", str(float(item1))],
    ["Item 2", str(float(item2))],
    ["Item 3", str(float(item3))],
    ["Combo 1(Item 1 + 2)", str(float(combo1))],
    ["Combo 2(Item 2 + 3)", str(float(combo2))],
    ["Combo 3(Item 1 + 3)", str(float(combo3))],
    ["Combo 4(Item 1 + 2 + 3)", str(float(combo4))]
  ]
  
  columns = ["Product(S)", "Price"]
  
  for column in columns:
    table.add_column(column)

  for row in rows:
    table.add_row(*row, style='bright_green')
  
  console = Console()
  console.print(table)
  print("----------------")
  print("For delivery Contact: 1234567890")

catalog()