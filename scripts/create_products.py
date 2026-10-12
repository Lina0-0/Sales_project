from utils.helpers import clean_lines, parse_products
from utils.product import Product

def main():
    with open("data/raw/data.txt", "r") as file:
        lines = file.readlines()
    
    cleaned_lines = clean_lines(lines)
    products = parse_products(cleaned_lines)

    total_sales = 0

    for name, price, quantity in products:
        p = Product(name, price, quantity)
        total_value = p.total_value()
        print(name ,":" , total_value)
        total_sales += total_value
        
    print("Total Sales: ", total_sales)

if __name__ == "__main__":
    main()