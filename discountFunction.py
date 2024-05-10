def calculate_discount(price, discount_percent): 
    if discount_percent >= 20:
        discount_price = price * (discount_percent / 100)
        final_price = price - discount_price
        print("Your final price after calculating the discount is:", final_price)
    else:
        final_price = price
        print("No discount applied.")

price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount: "))

print("Your initial price is:", price)
calculate_discount(price, discount_percent)
