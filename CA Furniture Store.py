# Furniture Names And Descriptions
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."


# Furniture Prices
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

# ------------------------------------------------------

# Sales Tax
sales_tax = .088

# ------------------------------------------------------

# Customer One Begin
customer_one_total = 0
customer_one_itemization = ""


# Customer One Items Purchaced
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description


# Customer One Check Out
customer_one_tax = customer_one_total * sales_tax
customer_one_final_total = customer_one_total + customer_one_tax


# Customer One Reciept Begin
# Customer One Purchase Itemization
print("""Customer One Items Purchased
""")
print(customer_one_itemization)

# Customer One cost
print("""
----------------------------------------""")
print("Subtotal: ""$",round(customer_one_total,2))
print("Tax: ""$",round(customer_one_tax,2))

# Customer One Total Price
print("Customer One Total: ""$",round(customer_one_final_total,2))
print("""
Have A Great Day :)""")

# ________________________________________________

print("""


-----------------------------------------------


""")

# Customer Two Begin
customer_two_total = 0
customer_two_itemization = ""


# Customer Two Items Purchaced
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description

customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description


# Customer Two Check Out
customer_two_tax = customer_two_total * sales_tax
customer_two_final_cost = customer_two_total + customer_two_tax


# Customer One Reciept Begin
# Customer One Purchase Itemization
print("""Customer Two Items Purchased
""")
print(customer_two_itemization)

# Customer Two cost
print("""
----------------------------------------""")
print("Subtotal: ""$",round(customer_two_total,2))
print("Tax: ""$",round(customer_two_tax,2))

# Customer Two Total Price
print("Customer Two Total: ""$",round(customer_two_final_cost,2))
print("""
Have A Great Day :)""")
