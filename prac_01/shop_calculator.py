"""
Shop Calculator
"""
# total_price = 0
# discount_price = 0
# total_items = int(input('Number of items: '))
# for item in range(1, total_items + 1, 1):
#     item_price = float(input('Price of item: '))
#     total_price = total_price + item_price
#     if total_price > 100:
#         discount_price = (total_price * 0.10)
# print(f'Total price for {total_items} items is ${total_price - discount_price:.2f}')

total_price = 0
discount_price = 0
total_items = int(input('Number of items: '))
while total_items < 0:
    print('Invalid number of items!')
    total_items = int(input('Number of items: '))
for item in range(1, total_items + 1, 1):
    item_price = float(input('Price of item: '))
    total_price = total_price + item_price # Total price of all items
    if total_price > 100:
        discount_price = (total_price * 0.10) # Compute the discount price
print(f'Total price for {total_items} items is ${total_price - discount_price:.2f}')



