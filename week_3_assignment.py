# Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage 
# (discount_percent) as parameters. If the discount is 20% or higher,
# apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter
# the original price of an item and the discount percentage. Print the 
# final price after applying the discount, or if no discount was applied, print the original price.


original_price = input("Enter the original price:" )
discount_percent = input("Enter the discounted percentage:" )

def calculate_discount(original_price, discount_percent):
  
  
  discount = int(discount_percent)/100*int(original_price)
  if int(discount_percent) >= 20:
    print(f"After discount was applied you will pay: ${int(original_price)- int(discount)}")
  else:
    print(f"Sorry there was no discount applied you must pay the original price ${original_price}")
    
calculate_discount(original_price, discount_percent)