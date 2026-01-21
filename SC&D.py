def final_price(price, tax_percent):
    return price + (price * tax_percent / 100)

print(final_price(100, 10))
