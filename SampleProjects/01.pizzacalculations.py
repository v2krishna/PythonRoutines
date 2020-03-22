import pandas as pd

pizzas = [
        "Hawaiian",
        "Champange Ham & Cheese",
        "Beef & Onion",
        "Pepperoni",
        "Cheese Pizza",
        "Bacon & Mushroom",
        "Italiono",
        "The Deluxe",
        "Ham, Egg & Hollandaise",
        "Aermicano",
        "Mr Wedge",
        "BBQ Meatlovers"
]

df = pd.DataFrame(pizzas, columns = ["Pizzas"])
df.loc[:8, "Prices"] = 7.50   # First 7 items
df.loc[8:, "Prices"] = 13.50  # all the rest
df.index += 1                 # So thats its not zero-indexed
total_bill = 0.0

print("Welcome to Pizza Planet")
print()
print("Here's our Menu")
print()

# https://stackoverflow.com/questions/25777037/how-can-i-left-justify-text-in-a-pandas-dataframe-column-in-an-ipython-notebook
print(df.to_string(justify = "left",
                   header = False,
                   formatters={
                       "Pizzas": "{{:<{}s}}".format(df['Pizzas'].str.len().max()).format,
                       "Prices":"    ${:.2f}".format
                              }
                   )
      )
print()
print("Input a number a presse enter to select an item")
print("Input 'done' to finish your order and tabulate your bill")
print("Input 'exit' to cancel your orders")

while True:
    order = input(">>>  ")
    if order == 'exit':
        print("Order has been cancelled")
        break
    elif order == 'done':
        print("Your total bill is ${:.2f}.".format(total_bill))
        input("Press any key to exit")
        break
    elif int(order) in df.index:
        item = df.loc[int(order), "Pizzas"] # get the respective items
        price = df.loc[int(order), "Prices"]  #by indexing order input
        print("You've selected {} ! That would be ${:.2f}.".format(item, price))
        total_bill += price
        continue
    else:
        print("Don't be an idiot")
        input("Press any key to exit")
        break
